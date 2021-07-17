import configparser


class User:
    username = None
    password = None
    email = None
    headers = None
    cookies = None
    account = None

    def __init__(self, username, password, email, headers, cookies):
        self.username = username
        self.password = password
        self.email = email
        self.headers = headers
        self.cookies = cookies


CONFIG = configparser.ConfigParser()
CONFIG.read('/home/matt/southwest-alerts/southwestalerts/config.ini')
USERNAME = CONFIG['southwest']['username']
PASSWORD = CONFIG['southwest']['password']

users = []
user = User(USERNAME, PASSWORD, None, None, None)
users.append(user)
