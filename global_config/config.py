from dotenv import load_dotenv
import os

from global_config.types import User

def load_config():
    environment = os.getenv('ENV', 'qa')  # Default to 'qa' if ENV is not set
    if environment == 'qa':
        dotenv_path = os.path.join(os.path.dirname(__file__), '.qa.env')
    elif environment == 'beta':
        dotenv_path = os.path.join(os.path.dirname(__file__), '.beta.env')
    else:
        raise ValueError(f"Unknown environment: {environment}")
    
    load_dotenv(dotenv_path=dotenv_path)


load_config()


base_url = os.getenv("PORTAL_URL", 'NONE')
user_name = os.getenv("USER_NAME",'NONE')
user_password = os.getenv("USER_PASSWORD",'NONE')

if user_name and user_password:
    user = User(user_name=user_name,password=user_password)

