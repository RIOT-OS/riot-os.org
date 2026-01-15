#!/usr/bin/env python3

import os
import sys
import json
import re
import shlex
import subprocess
import glob
from string import Template

try:
    import requests
except ImportError:
    requests = None

from default_data import (
    DEFAULT_BOARDS, DEFAULT_CPUS, DEFAULT_DRIVERS,
    DEFAULT_DRIVER_CATEGORIES, DEFAULT_CONTRIBUTORS, DEFAULT_STATS,
    DEFAULT_MAINTAINERS,
)

DATA_DIR = os.getenv("DATA_DIR", os.path.join(os.path.abspath(__file__)))
DEFAULT_RIOT_BASE = os.path.join(os.path.abspath(__file__), "_RIOT")
RIOTBASE = os.path.abspath(os.getenv("RIOTBASE", DEFAULT_RIOT_BASE))

RIOT_DOC_BASE_URL = "https://api.riot-os.org"
TEMPLATE_BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#
# Data files templates
#
BOARDS_TEMPLATE = """- name: ${name}
  apiurl: ${doc_url}/group__boards__${group}.html
"""

CPU_TEMPLATE = """- name: ${name}
  apiurl: ${doc_url}/group__cpu__${group}.html
"""

DRIVERS_TEMPLATE = """- name: ${name}
  parent: drivers_${parent}
  apiurl: ${doc_url}/group__drivers__${group}.html
"""

DRIVER_CATEGORIES_TEMPLATE = """- name: ${name}
  group: drivers_${group}
  apiurl: ${doc_url}/group__drivers__${group}.html
"""

CONTRIBUTORS_TEMPLATE = """- login: ${login}
  avatar_url: ${avatar_url}
  html_url: https://github.com/${login}
"""

STATS_TEMPLATE = """boards: ${boards}
cpus: ${cpus}
commits: ${commits}
"""

MAINTAINERS_TEMPLATE = """- login: ${login}
  avatar_url: ${avatar_url}
  html_url: https://github.com/${login}
  name: ${name}
  admin: ${admin}
  owner: ${owner}
  areas: ${areas}
"""

TEMPLATES = {
    "boards": BOARDS_TEMPLATE,
    "cpus": CPU_TEMPLATE,
    "drivers": DRIVERS_TEMPLATE,
    "drivers_cats": DRIVER_CATEGORIES_TEMPLATE,
    "contributors": CONTRIBUTORS_TEMPLATE,
    "stats": STATS_TEMPLATE,
    "maintainers": MAINTAINERS_TEMPLATE,
}


CONTRIBUTORS_URL = "https://api.github.com/repos/RIOT-OS/RIOT/contributors"
OBJ_PER_PAGE = 100
MAX_PAGES = 20


def fetch_contributors_data():
    """Fetch the complete list of RIOT contributors via the GitHub API."""
    # Return default contributors if requests module is not available
    if requests is None:
        print(
            "Warning: 'requests' package is missing, default contributors "
            "will be returned (only 10 contributors).\nYou can install "
            "'requests' using 'make install_python_requirements'."
        )
        return DEFAULT_CONTRIBUTORS
    current_page = 0
    contributors_data = []
    headers = {}
    token = os.getenv("GITHUB_TOKEN")
    if token is not None:
        headers["Authorization"] = f"token {token}"
    for _ in range(MAX_PAGES):
        try:
            request = requests.get(
                CONTRIBUTORS_URL,
                params={"page": current_page, "per_page": OBJ_PER_PAGE},
                headers=headers
            )
            data = json.loads(request.content)
            if request.status_code != requests.codes.ok:
                return DEFAULT_CONTRIBUTORS
        except:
            return DEFAULT_CONTRIBUTORS

        if not data:
            break

        contributors_data += data
        current_page += 1

    fetched_contributors = {
        data["login"]: data["avatar_url"] for data in contributors_data
    }

    return [
        { "login": login, "avatar_url": url }
        for login, url in fetched_contributors.items()
    ]


def fetch_maintainer_data():
    if requests is None:
        print(
            "Warning: 'requests' package is missing, default contributors "
            "will be returned (only 10 contributors).\nYou can install "
            "'requests' using 'make install_python_requirements'."
        )
        return DEFAULT_MAINTAINERS
    if not os.getenv("GITHUB_TOKEN"):
        print(
            "Warning: no GitHub token provided via GITHUB_TOKEN environment "
            "variable, default maintainers will be returned (only 6 "
            "maintainers).\nYou need a GitHub personal access token with "
            "admin:org > read:org scope."
        )
        return DEFAULT_MAINTAINERS
    maintainers = get_team_members("maintainers")
    admins = get_team_members("admin")
    owners = get_team_members("owners")
    maintainers = maintainers.union(admins)
    maintainers = maintainers.union(owners)
    maintainer_areas = get_maintainer_codeowner_patterns(maintainers)
    res = []
    for maintainer in maintainer_areas:
        github_profile = get_github_user(maintainer)
        if "login" not in github_profile or github_profile["login"] != maintainer:
            print(
                "Warning: error on fetching GitHub profile. Make sure "
                "the GITHUB_TOKEN has appropriate rights"
            )
            return DEFAULT_MAINTAINERS
        res.append(
            {
                "login": maintainer,
                "name": github_profile["name"] if github_profile["name"] else "",
                "avatar_url": github_profile["avatar_url"],
                "html_url": github_profile["html_url"],
                "admin": maintainer in admins,
                "owner": maintainer in owners,
                "areas": list(sorted(maintainer_areas[maintainer])),
            }
        )
    return res


def search_data(file_paths, regexp, parent_regexp=None, multi=False):
    """Search doxygen data in a list of files/dirs using regexps."""
    results = []
    for path in file_paths:
        # Try to extract data from Doxygen defgroup/ingroup comments
        with open(path) as search_file:
            # Only keep lines with defgroup/ingroup doxygen tags
            content = [
                l.strip() for l in search_file.readlines()
                if re.match(r"^.*(@defgroup|@ingroup).*$", l)
            ]
        for idx, line in enumerate(content):
            if "@defgroup" in line:
                match = re.match(regexp, line)
                if match is None:
                    if multi is True:
                        continue
                    else:
                        break
                name = match.group(2)
                group = match.group(1).replace("_", "__")
                result = { "name": f"\"{name}\"", "group": group }
                if parent_regexp is not None:
                    # @ingroup should be on the next line
                    if idx + 1 == len(content):
                        match = re.match(parent_regexp, content[idx - 1])
                    else:
                        match = re.match(parent_regexp, content[idx + 1])
                    if match is not None:
                        result.update({
                            "parent": match.group(1).replace("_", "__")
                        })
                    else:
                        result.update({"parent": ""})
                results += [result]
                if multi is True:
                    continue
                else:
                    break
    return results


def render_data_to_file(name, data):
    """Render data to a file using a string template."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    data_file = os.path.join(DATA_DIR, f"riot_{name}.yml")
    with open(data_file, "w") as f_dest:
        f_dest.write("# File generated automatically, please don't edit!!\n")
        for elem in data:
            template = Template(TEMPLATES[name])
            elem.update({"doc_url": RIOT_DOC_BASE_URL})
            f_dest.write(template.substitute(**elem))


def _subdirs(dirname, exclude=set()):
    for _, dirnames, _ in os.walk(os.path.join(RIOTBASE, dirname)):
        break
    return sorted(set(dirnames) - exclude)


def fetch_boards_data():
    """Fetch all boards Doxygen description data (name, doxygen group)."""
    boards_doc = [
        os.path.join(RIOTBASE, line.split(":")[0])
        for line in subprocess.check_output(
            shlex.split(f"git -C {RIOTBASE} grep -n '@defgroup\\s*boards_'")
        ).decode()[:-1].split("\n")
    ]
    boards = search_data(boards_doc, r"^.*boards_([a-zA-Z0-9\-_\.]+)[ ]+(.*)$")
    # Some board groups are not relevant and have to be removed
    return [board for board in boards if not "common" in board["group"]]


def fetch_cpus_data():
    """Fetch all cpus Doxygen description data (name, doxygen group)."""
    files = [
        "doc.md",
        os.path.join("include", "cpu.h"),
        os.path.join("include", "cpu_conf.h"),
        os.path.join("include", "periph_cpu.h"),
    ]
    cpu_doc = [
        os.path.join(RIOTBASE, "cpu", cpu_path, file_path)
        for cpu_path in _subdirs("cpu") for file_path in files
        if os.path.exists(os.path.join(RIOTBASE, "cpu", cpu_path, file_path))
    ]
    cpus = search_data(cpu_doc, r"^.*cpu_([a-zA-Z0-9\-_\.]+)[ ]+(.*)$")
    # Some cpu names/groups are not relevant and have to be removed or need
    # cleanup
    return [
        cpu for cpu in cpus
        if (
            not cpu["group"].endswith("conf") and
            not "common" in cpu["name"].lower() and
            not "common" in cpu["group"]
        )
    ]


def fetch_drivers_data():
    """Fetch all drivers Doxygen description data."""
    drivers_doc = set([
        os.path.join(RIOTBASE, line.split(":")[0])
        for line in subprocess.check_output(
            shlex.split(f"git -C {RIOTBASE} grep -n '@defgroup\\s*drivers_'")
        ).decode()[:-1].split("\n")
    ])
    # Search in all defined paths
    drivers = search_data(
        drivers_doc,
        r"^.*drivers_([a-zA-Z0-9\-_\.]+)[ ]+(.*)$",
        parent_regexp=r"^.*drivers_([a-zA-Z0-9\-_\.]+).*$",
    )
    return [
        driver for driver in sorted(drivers, key=lambda elem: elem["group"])
        if not driver["group"].endswith("config")
    ]


def fetch_driver_categories_data():
    """Fetch all drivers categories description data (name, doxygen group)."""
    driver_categories_all = search_data(
        [
            os.path.join(RIOTBASE, "drivers", "doc.txt"),
            os.path.join(RIOTBASE, "drivers", "include", "periph", "doc.txt")
        ],
        r"^.*drivers_([a-zA-Z0-9\-_\.]+)[ ]+(.*)$",
        multi=True
    )
    return [
        category for category in driver_categories_all
        if not "Configurations" in category["name"]
    ]


def fetch_stats_data():
    """Fetch stats data (name, doxygen group)."""
    cpus = 0
    for kconfig in glob.glob(
        os.path.join(RIOTBASE, "cpu/**/Kconfig"), recursive=True
    ): 
        with open(kconfig) as config: 
            content = config.readlines()
        for line in content: 
            if re.match(r"config CPU_FAM_(\w)", line) is not None: 
                cpus = cpus + 1
    commits = int(subprocess.check_output(
        shlex.split(f"git -C {RIOTBASE} rev-list HEAD --count")
    ))
    return {
        "boards": len(_subdirs("boards", exclude=set(["common"]))),
        "cpus": cpus, "commits": commits
    }


def get_next_page(response):
    if "Link" not in response.headers:
        return None
    links = re.split(r",\s*", response.headers["Link"])
    for link in links:
        params = re.split(r";\s*", link)
        link_match = re.match("^<(.*)>$", params[0])
        for param in params:
            if param == 'rel="next"' and link_match:
                return link_match[1]
    return None

def get_team_members(team):
    token = os.getenv("GITHUB_TOKEN")
    assert token is not None
    members = requests.get(
        f"https://api.github.com/orgs/RIOT-OS/teams/{team}/members",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    res = set()
    while members:
        try:
            res = res.union(set(m["login"] for m in members.json()))
        except Exception as exc:
            print(f"Error fetching team {team}: {exc}", file=sys.stderr)
            raise
        next_page = get_next_page(members)
        if not next_page:
            break
        members = requests.get(
            next_page,
            headers={
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {token}",
                "X-GitHub-Api-Version": "2022-11-28",
            },
        )
    return res


def get_github_user(username):
    token = os.getenv("GITHUB_TOKEN")
    assert token is not None
    user = requests.get(
        f"https://api.github.com/users/{username}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    return user.json()


def get_maintainer_codeowner_patterns(maintainers):
    maintainer_patterns = {m: set() for m in maintainers}

    with open(os.path.join(RIOTBASE, "CODEOWNERS")) as codeowners_file:
        for line in codeowners_file:
            if re.search(r"^\s*#", line) or re.match(r"^\s*$", line):
                # skip comments and empty lines
                continue
            pattern, *owners = re.split(r"\s+", line.strip())
            for owner in owners:
                owner = owner.lstrip("@")
                if owner in maintainer_patterns:
                    maintainer_patterns[owner].add(pattern.lstrip("/"))
    return maintainer_patterns


def main():
    """Main function."""
    if not os.path.exists(RIOTBASE):
        boards = DEFAULT_BOARDS
        cpus = DEFAULT_CPUS
        drivers = DEFAULT_DRIVERS
        driver_categories = DEFAULT_DRIVER_CATEGORIES
        contributors = DEFAULT_CONTRIBUTORS
        maintainers = DEFAULT_MAINTAINERS
        stats = DEFAULT_STATS
    else:
        sys.stdout.write("Generating RIOT data files... ")
        sys.stdout.flush()
        boards = fetch_boards_data()
        cpus = fetch_cpus_data()
        drivers = fetch_drivers_data()
        driver_categories = fetch_driver_categories_data()
        contributors = fetch_contributors_data()
        maintainers = fetch_maintainer_data()
        stats = fetch_stats_data()
    for name, data in (
        ("boards", boards), ("cpus", cpus), ("drivers", drivers),
        ("drivers_cats", driver_categories), ("contributors", contributors),
        ("stats", [stats]), ("maintainers", maintainers)
    ):
        render_data_to_file(name, data)
    if os.path.exists(RIOTBASE):
        print("done!")


if __name__ == "__main__":
    main()
