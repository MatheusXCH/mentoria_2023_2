import os

from dotenv import load_dotenv

load_dotenv()

INSTANCIA_GERENCIADA = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "name": os.getenv("DB_NAME"),
}

INSTANCIA_VM = {
    "user": os.getenv("DB_USER_VM"),
    "password": os.getenv("DB_PASSWORD_VM"),
    "host": os.getenv("DB_HOST_VM"),
    "port": os.getenv("DB_PORT_VM"),
    "name": os.getenv("DB_NAME_VM"),
}
