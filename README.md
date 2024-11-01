# Тестовое задание на мониторинг курса доллара
## Как запустить проект

* Примечание:
команды выше приведены для ОС Linux. Если Вы используете ОС Windows, то используйте "python" вместо "python3"
и `source venv/Scripts/activate` (для активации виртуального окружения).

Клонировать репозиторий и перейти в него в командной строке:
```commandline
git clone git@github.com:LeoNefesch/usd_rate_test_task.git
```
```commandline
cd usd_rate_test_task
```
Создать файл .env с таким содержимым:
```commandline
SECRET_KEY=<сгенерируй, например, здесь: https://djecrety.ir/>
DEBUG=True  # turn to False for production
ALLOWED_HOSTS=127.0.0.1,localhost
```
Cоздать и активировать виртуальное окружение:
```commandline
python3 -m venv venv
```
```commandline
source venv/bin/activate
```
Обновить pip и установить зависимости:
```commandline
python3 -m pip install --upgrade pip
```
```commandline
pip install -r requirements.txt
```
Создать в корне проекта файл db.sqlite3 (в случае с локальной разработкой).
Создать миграции в БД:
```commandline
python3 manage.py makemigrations
```
Применить миграции:
```commandline
python3 manage.py migrate 
```
Запустите сервер
```commandline
python3 manage.py runserver
```