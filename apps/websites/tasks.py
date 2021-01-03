import os
import requests

from config import celery_app

from .models import Website
from .xlsl_utils import parse_website_list_xlsx


@celery_app.task(ignore_result=True)
def import_website_urls():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(BASE_DIR, "apps", "websites", "fixtures", "websites.xlsx")

    websites_list, errors = parse_website_list_xlsx(file_path=file_path)
    for url in websites_list:
        Website.objects.get_or_create(url=url)
    
    print(errors)


@celery_app.task()
def load_websites_excel(url=None):
    if not url:
        url = "https://uca49b388e165e867dad0478dfce.dl.dropboxusercontent.com/cd/0/get/BGNmFfSiUWYE-0oZUD6OQbaNP7DptElKvs6IGjH1ixV23JyWgf2meWxNAgA_yW2u35W2L9ooZWS_Eus5bblBJvdnRggdf5vWHHvJnqg4Y21kwVzJf8UGFI_g7r8fTRXLi4M/file?_download_id=4019830210719888239647509883093788546475447251767401055556324143&_notify_domain=www.dropbox.com&dl=1"
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(BASE_DIR, "apps", "websites", "fixtures", "websites.xlsx")

    session = requests.Session()

    response = session.request("GET", url)

    # print(response.content)
    websites_file = open(file_path, 'wb')
    websites_file.write(response.content)
