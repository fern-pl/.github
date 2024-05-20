# We need to clone each repo to get the stats we need, the github api is not good enough

import os
import pytz
import subprocess
import requests
import tempfile
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

realDir = os.path.dirname(os.path.realpath(__file__))


def bytes_to_human_readable(bytes_num):
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']
    unit_index = 0
    while bytes_num >= 1024 and unit_index < len(units) - 1:
        bytes_num /= 1024.0
        unit_index += 1
    return f"{round(bytes_num, 2)}_{units[unit_index]}"

def get_cmd(cmdList):
    result = subprocess.run(cmdList, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout.strip()
    else:
        print("Error:", result.stderr)
        return None


def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return sum(1 for line in file)
    except UnicodeDecodeError:
        return 0

def count_lines_in_directory(directory):
    total_lines = 0
    for dirpath, _, filenames in os.walk(directory):
        if ".git" in dirpath:
            continue
        for filename in filenames:
            if filename in [".gitignore", "LICENSE.txt", "dub.json", "dub.selections.json"]:
                continue
            file_path = os.path.join(dirpath, filename)
            total_lines += count_lines_in_file(file_path)
    return total_lines

# print(count_lines_in_directory("/tmp/tmp_bgj3xtx/fnc"))


def size_stats_by_repo(org, repo):
    dirpath = tempfile.mkdtemp()
    os.chdir(dirpath)

    repoStr = org + "/" + repo
    os.system("git clone https://github.com/" + repoStr)

    lines = count_lines_in_directory(repo)
    os.chdir(repo)
    
    commitCount = get_cmd(['git', 'rev-list', '--all', '--count'])
    return lines, int(commitCount)

def getJson(url):
    return requests.get(url).json()
def api_stats_by_repo(org, repo):
    apiUrl = "https://api.github.com/repos/" + org + "/" + repo

    futures = {}
    with ThreadPoolExecutor(max_workers = 999) as exe:
        futures["main"] = exe.submit(getJson, apiUrl)
        futures["langs"] = exe.submit(getJson, apiUrl + "/languages")
    results = {k:v.result() for k, v in futures.items()}
    codeSize = sum(v for k, v in results["langs"].items())

    print(results["main"]["updated_at"])
    dt = datetime.strptime(results["main"]["updated_at"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=pytz.utc)
    return {
        "codeSize": codeSize,
        "repoSize": results["main"]["size"]*1024,
        "stars": results["main"]["stargazers_count"],
        "lastMod":  dt
    }
def main():
    repos = [
        ["fern-pl", "fnc"],
        ["fern-pl", "gallinule"], 
        ["fern-pl", "specification"],
        ["fern-pl", "standard-library"],
        ["fern-pl", "runtime"],
    ]
    data = {
        "lines": 0,
        "commits": 0,
        "codeSize": 0,
        "repoSize": 0,
        "stars": 0,
        "lastMod": None
    }
    for repo in repos:
        lines, commits = size_stats_by_repo(*repo)
        data["lines"] += lines
        data["commits"] += commits

        stats = api_stats_by_repo(*repo)
        for k, v in stats.items():
            if k != "lastMod":
                data[k]=v + (data[k] | 0)
        if data["lastMod"] is None:
            data["lastMod"] = stats["lastMod"]
        else:
            data["lastMod"] = max(data["lastMod"], stats["lastMod"])

    os.chdir(realDir)

    est_timezone = pytz.timezone('America/New_York')
    est_time = data["lastMod"].astimezone(est_timezone)

    # Format the EST time
    est_time_str = est_time.strftime("%m/%d/%Y_%I:%M:%S_%p_%Z")


    os.system(f"curl \"https://img.shields.io/badge/Total_Stars-{data['stars']}-gold\" > output/stars.svg")
    os.system(f"curl \"https://img.shields.io/badge/Total_Lines-{data['lines']}-blue\" > output/lines.svg")
    os.system(f"curl \"https://img.shields.io/badge/Total_Commits-{data['commits']}-blue\" > output/commits.svg")
    os.system(f"curl \"https://img.shields.io/badge/Total_Code_Size-{bytes_to_human_readable(data['codeSize'])}-blue\" > output/codeSize.svg")
    os.system(f"curl \"https://img.shields.io/badge/Total_Repo_Size-{bytes_to_human_readable(data['repoSize'])}-blue\" > output/repoSize.svg")
    os.system(f"curl \"https://img.shields.io/badge/Latest_Commit-{str(est_time_str)}-blue\" > output/lastMod.svg")



    print(est_time_str)



if __name__ == "__main__":
    main()
