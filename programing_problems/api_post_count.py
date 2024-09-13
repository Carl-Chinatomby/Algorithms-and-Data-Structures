#  API Call Response parser
# https://jsonplaceholder.typicode.com/users
# https://jsonplaceholder.typicode.com/posts

# How many times has Kurtis Weissnat posted?
import requests
import json


USERS_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'


def find_user_id(name):
    resp = requests.get(USERS_URL)
    users = json.loads(resp.content)
    for user in users:
        if user['name'].lower() == name.lower():
            return user['id']


def get_post_count_by_id(user_id):
    resp = requests.get(POSTS_URL)
    posts = json.loads(resp.content)
    count = 0
    for post in posts:
        if post['userId'] == user_id:
            count += 1

    return count



def main():
    user_id = find_user_id('Kurtis Weissnat')
    print(user_id)
    post_cnt = get_post_count_by_id(user_id)
    print(post_cnt)

main()
