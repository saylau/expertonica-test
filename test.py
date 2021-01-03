import requests
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "apps", "live_probes", "fixtures", "websites.xlsx")

session = requests.Session()

response = session.request("GET", "https://uca49b388e165e867dad0478dfce.dl.dropboxusercontent.com/cd/0/get/BGNmFfSiUWYE-0oZUD6OQbaNP7DptElKvs6IGjH1ixV23JyWgf2meWxNAgA_yW2u35W2L9ooZWS_Eus5bblBJvdnRggdf5vWHHvJnqg4Y21kwVzJf8UGFI_g7r8fTRXLi4M/file?_download_id=4019830210719888239647509883093788546475447251767401055556324143&_notify_domain=www.dropbox.com&dl=1")

# print(response.content)
websites_file = open(file_path, 'wb')
websites_file.write(response.content)
# print(response.__dict__)