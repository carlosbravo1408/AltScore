import os
from typing import Optional, Any

from dotenv import load_dotenv


class _Constants:
    _instance: Optional["_Constants"] = None
    __OPTIONS = {"API_KEY", "PORT"}

    def __new__(cls, dotenv_path: str = "./.env") -> "_Constants":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__load(dotenv_path)
        return cls._instance

    def __load(self, dotenv_path: str) -> None:
        load_dotenv(dotenv_path)
        self.__vars = dict(os.environ)

    def get(self, key: str, default=None) -> Any:
        if key in self.__OPTIONS:
            return self.__vars.get(key, default)
        return default

    def __getattr__(self, key: str) -> Any:
        return self.get(key)


Constants = _Constants()
