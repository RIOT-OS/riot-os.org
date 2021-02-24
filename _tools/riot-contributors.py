import os
import sys
import json
import requests

CONTRIBUTORS_URL = "https://api.github.com/repos/RIOT-OS/RIOT/contributors"
OBJ_PER_PAGE = 100
MAX_PAGES = 20

if __name__ == "__main__":
    curr_page = 0
    contributor_list = []
    headers = {}
    token = os.getenv('GITHUB_TOKEN')
    if token:
        headers["Authorization"] = "token {}".format(token)

    for _ in range(MAX_PAGES):
        request = requests.get(CONTRIBUTORS_URL,
                               params={"page": curr_page,
                                       "per_page": OBJ_PER_PAGE},
                               headers=headers)
        data = json.loads(request.content)

        if request.status_code != requests.codes.ok:
            sys.exit("Github API status code ({}) != OK".format(request.status_code))

        if len(data) == 0:
            break

        contributor_list += data
        curr_page += 1

    sys.stdout.write(json.dumps(contributor_list))
