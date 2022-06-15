"""
"""

import re
def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')


domain_name('http://www.yandex.ru')


def domain_name(url):
    headers = ["http://", "https://", "www.", "http://www", "https://www."]
    for header in headers:
        if header in url:
            url = url.replace(header, "")
    domain = url.split(".")[0]
    return domain

import re
def domain_name(url):
    result = re.search("(//)?(([a-zA-Z0-9_-]+)\.)+", url)
    return result.group(3) if result else None