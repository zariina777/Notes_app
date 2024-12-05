from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://postgres:2908@localhost:5433/notes_db"

    class Config:
        env_file = ".env" #файл который не хранится ни где кроме как локально на пк при разрабоке проекта
                          # и на сервере вместе с проектом
                          # хранятся там все ключи пароли логины необходимы для раьоты проекта
settings = Settings() # создали объект от класса Сеттингс, при создании объекта класа сеттингс
                      # все переменные можно иницилизировать от файла ЕНф