import os

from dotenv import load_dotenv


class _Constants:
    _instance = None
    __OPTIONS = {"API_KEY", "PORT"}

    def __new__(cls, dotenv_path: str = "./.env"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__load(dotenv_path)
        return cls._instance

    def __load(self, dotenv_path: str):
        load_dotenv(dotenv_path)
        self.__vars = dict(os.environ)

    def get(self, key: str, default=None):
        if key in self.__OPTIONS:
            return self.__vars.get(key, default)
        return default

    def __getattr__(self, key: str):
        return self.get(key)


Constants = _Constants()
