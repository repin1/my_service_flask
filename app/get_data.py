"""
    There is func to get json data from git hub and auth list with your login and psswd
"""
from json import loads, dumps
from requests import get
auth_list = []


# func to return json from github
def get_data(name="lena"):
    user_url = r'https://api.github.com/users/{}/repos'.format(name)
    if len(auth_list) != 0:
        response = get(user_url, auth=tuple(auth_list))
    else:
        response = get(user_url)
    return dumps(loads(response.content.decode("utf-8")), sort_keys=True, indent=4)
