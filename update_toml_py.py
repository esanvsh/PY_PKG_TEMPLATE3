import os
import toml
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

PROJECT_NAME = os.getenv("PROJECT_NAME")
REPO_NAME = os.getenv("REPO_NAME")
GITHUB_USER_NAME = os.getenv("GITHUB_USER_NAME")
AUTHOR_NAME = os.getenv("AUTHOR_NAME")
AUTHOR_EMAIL = os.getenv("AUTHOR_EMAIL")
PACKAGE_NAME = os.getenv("PACKAGE_NAME")
LICENCSE_NAME = os.getenv("LICENCSE_NAME")
PYTHON_VERSION = os.getenv("PYTHON_VERSION")
YEAR = os.getenv("YEAR")
COMMAND_NAME = os.getenv("COMMAND_NAME")
if not all([PROJECT_NAME, REPO_NAME, GITHUB_USER_NAME, PACKAGE_NAME, AUTHOR_NAME, AUTHOR_EMAIL, LICENCSE_NAME, PYTHON_VERSION]):
    raise Exception("One or more environment variables are not set")

#print(os.path.abspath(os.getcwd()))
MY_TOML_TEMP_FILE = os.path.join(os.path.dirname(__file__), 'pyproject_temp.toml')
MY_TOML_FILE = os.path.join(os.path.dirname(__file__), 'pyproject.toml')
#print(MY_FILE)
with open(MY_TOML_TEMP_FILE, 'r') as f:
    config = toml.load(f)
#print(config)
#print(config['project']['authors'])
#print([{"name":GITHUB_USER_NAME, "email":AUTHOR_EMAIL},])
config['project']['authors'] = [{"name":GITHUB_USER_NAME, "email":AUTHOR_EMAIL},]
config['project']['license'] = {"text":LICENCSE_NAME}
config['project']['urls']['Documentation'] = "https://" + str(GITHUB_USER_NAME) +".github.io/"+ str(REPO_NAME) +"/"
config['project']['urls']['Source'] = "https://github.com/"+ str(GITHUB_USER_NAME)+"/"+str(REPO_NAME)+"/"
config['project']['urls']['Bug Tracker'] = "https://github.com/"+str(GITHUB_USER_NAME)+"/"+str(REPO_NAME)+"/issues"
config['project']['scripts'] = {str(COMMAND_NAME): str(PACKAGE_NAME)+".__main__:main"}
with open(MY_TOML_FILE, "w") as f:
    toml.dump(config, f)