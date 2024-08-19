import re

def extract_url(message):
    """
    Extract an URL from a given string.

    :param message: The input string containing the URL
    :return: The extracted URL
    """
    url_pattern = re.compile(r'https?://[^\s]+')
    
    url_match = url_pattern.search(message)
    
    if url_match:
        url = url_match.group(0)
        return url

#message = ""
#print(extract_url(message))