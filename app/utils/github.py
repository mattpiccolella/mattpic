from flask import jsonify
import requests, json
import random

ROOT_ENDPOINT = "https://api.github.com"
REPOS = "repos"
USERS = "users"
USER = "mjp2220"
LANGUAGES = "languages"

def github_language_data():
  repo_names = [repo['name'] for repo in fetch_repos()]
  languages = [fetch_languages(name) for name in repo_names]
  language_data = {}
  for name, language in zip(repo_names,languages):
    for lang in language:
      count = language[lang]
      if not lang in language_data:
        language_data[lang] = {}
        language_data[lang]['total'] = 0
      language_data[lang][name] = count
      language_data[lang]['total'] += count
  with open('languages.json', 'w') as output:
    json.dump(language_data,output)

def fetch_repos():
  repo_url = construct_request_url(ROOT_ENDPOINT,USERS,USER,REPOS)
  return requests.get(repo_url).json()

def fetch_languages(name):
  language_url = construct_request_url(ROOT_ENDPOINT,REPOS,USER,name,LANGUAGES)
  return requests.get(language_url).json()

def construct_request_url(*args):
  return '/'.join(str(i) for i in args)

if __name__ == '__main__':
  github_language_data()