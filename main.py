import requests

URLS = [
    "https://google.com",  # 200
    "https://www.linkedin.com/asdasdas",  # 404,
    "https://reston.com.ua/",
    "https://localhost:8082/",

]
TIMEOUT = 5


def check_non_available_domains(urls, timeout=None):
    no_available = []
    for url in urls:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code != requests.codes.ok:
                no_available.append(url)
        except requests.exceptions.RequestException:
            no_available.append(url)
    return no_available


print(check_non_available_domains(URLS))
