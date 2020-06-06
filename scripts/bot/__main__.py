import uuid
from random import randint
import requests

from .config import *


class User:
    def __init__(self, username):
        self.username = username
        self.email = f'{username}@gmail.com'
        self.token = None

    def get_credentials(self):
        return {
            'username': self.username,
            'email': self.email,
            'password': CUSTOM_USER_PASSWORD
        }

    def singup_user(self):
        print("--- User Signup ---")
        response = requests.post(SIGNUP_URL, json=self.get_credentials())
        print(f"Request to: {response.url}, status: {response.status_code}\n")
        return response

    def login_user(self):
        print("--- User Login ---")
        response = requests.post(LOGIN_URL, json=self.get_credentials())
        if response.status_code == 201:
            self.token = response.json()['data'].get('token')
        print(f"Request to: {response.url}, status: {response.status_code}\n")
        return response

    def create_login_user(self):
        self.singup_user()
        self.login_user()


class Bot:
    tokens = []
    post_ids = []

    def create_posts(self, token):
        header = {"Authorization": f"JWT {token}"}
        for i in range(randint(1, MAX_POST_PER_USER)):
            title = f"Post Title-{i}"
            data = {
                "title": title,
                "text": POST_TEXT,
            }
            print("--- Creating Post ---")
            response = requests.post(CREATE_POST_URL, json=data, headers=header)
            print(f"Request to: {response.url}, status: {response.status_code}\n")
            if response.status_code == 201:
                self.post_ids.append(response.json()['data'].get('id'))

    def like_post(self, token, post_id):
        header = {"Authorization": f"JWT {token}"}
        for i in range(randint(1, MAX_LIKE_PER_USER)):
            data = {
                "post_id": post_id,
            }
            print("--- Like Post ---")
            response = requests.post(LIKE_POST_URL, json=data, headers=header)
            print(f"Request to: {response.url}, status: {response.status_code}\n")

    def generate_users(self):
        user_names = (f"user-{uuid.uuid1().hex}" for _ in range(5))
        for name in user_names:
            user = User(username=name)
            user.create_login_user()
            self.tokens.append(user.token)

    def run(self):
        self.generate_users()
        for token in self.tokens:
            self.create_posts(token)
            for post_id in self.post_ids:
                self.like_post(token, post_id)
        print("--- Test Completed ---")


def main():
    bot = Bot()
    bot.run()


if __name__ == "__main__":
    main()
