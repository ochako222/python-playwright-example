from dotenv import load_dotenv
import os

from global_config.types import User


load_dotenv()

base_url = os.getenv("BASE_URL") or 'https://studio-elevate.qa.xyleme.com'
user_name=os.getenv("USER_NAME") or 'oleksandr.chako@xyleme.com'
user_password=os.getenv("USER_PASSWORD") or 'Mypass@123'

user = User(user_name=user_name,password=user_password)