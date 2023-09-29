#!/usr/bin/python3
"""The script takes 2 arguments and prints all the commits by:
    `<sha>: <author name>` one per line
    - The first argument is the "repository name"
    - The second argument is the "owner name"
"""
import sys
import requests


if __name__ == '__main__':
    url_fmt = "https://api.github.com/repos/{}/{}/commits"
    url = url_fmt.format(sys.argv[1], sys.argv[2])
    res = requests.get(url)
    commits = res.json()

    sorted_commits = sorted(
            commits,
            key=lambda x: x.get('commit').get('author').get('date'),
            reverse=True
        )

    counter = 0
    for commit in sorted_commits:
        if (counter == 10):
            break
        sha = commit.get('sha')
        committer = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(sha, committer))
        counter += 1
