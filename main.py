import configparser
config = configparser.ConfigParser()

config.read("config.cfg")

login = config.get('DEV', 'login')

print(login)
