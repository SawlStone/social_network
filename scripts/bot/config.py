NUMBER_OF_USERS = 5
MAX_POST_PER_USER = 10
MAX_LIKE_PER_USER = 5


POST_TEXT = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et 
dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip."""


API_URL = "http://127.0.0.1:8000/api"
SIGNUP_URL = f"{API_URL}/auth/user/signup/"
LOGIN_URL = f"{API_URL}/auth/user/login/"
CREATE_POST_URL = f"{API_URL}/post/create/"
LIKE_POST_URL = f"{API_URL}/post/like/"

CUSTOM_USER_PASSWORD = "12345"
