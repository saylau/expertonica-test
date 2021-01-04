import os
import requests

from config import celery_app
from apps.websites.models import Website

from .serializers import LiveProbeSerializer

session = requests.Session()


@celery_app.task()
def take_live_probes():
    """
    Launch Live Probe tasks for all websites in database
    """
    websites = Website.objects.all()
    for website in websites:
        try: 
            take_live_probe.delay(website.url, website.id)
        except Exception as exc:
            print(exc)


@celery_app.task()
def take_live_probe(url, id):
    """
    Take Live Probe for website
    """
    live_probe = {
        "website": id
    }

    try: 
        response = session.request('GET', url if url.startswith('http') else f'https://{url}', stream=True)
        print(response.elapsed.microseconds/1000)
        live_probe['response_time'] = int(response.elapsed.microseconds/1000)

        ip, port = response.raw._connection.sock.getsockname()
        live_probe['ip_address'] = f"{ip}:{port}"
        
        http_status_code = response.status_code
        live_probe['http_status_code'] = http_status_code
        
    except requests.Timeout as exc:
        print(exc)
        live_probe['is_timeout'] = True
        live_probe['error_type'] = 'Timeout'
    except requests.TooManyRedirects as exc:
        print(exc)
        live_probe['error_type'] = 'TooManyRedirects'
    except requests.ConnectionError as exc:
        print(exc)
        live_probe['error_type'] = 'ConnectionError'
    except Exception as exc:
        print(exc)
    finally:
        serializer = LiveProbeSerializer(data=live_probe)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return serializer.data
