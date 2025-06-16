import os
from dotenv import load_dotenv


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../.."))
env_path = os.path.join(project_root, ".env")

load_dotenv(dotenv_path=env_path)

DATABASE_URL = os.getenv('DATABASE_URL')
echo = True # Отображение SQL-запросов
