# Яндекс.Практикум

# курс Python-разработчик

## студент  Липатов Павел

## Учебный проект sprint_8.  CRUD для Yatube.

***

Задачи проекта:

В проекте **api_yatube** присутствует приложение posts с описанием моделей **Yatube**. Необходимо реализовать API для всех моделей.

Обязательно: работать с моделью **Post** через **ModelViewSet**.
***

Разворачивание проекта:

Клонировать репозиторий и перейти в его папку в командной строке:

```
git clone https://github.com/Juniee5/api_yatube
cd api_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

Для *lix-систем и MacOS:

```
source venv/bin/activate
```

Для windows-систем:

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:

```
cd yatube_api
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Создать суперпользователя Django:

```
python3 manage.py createsuperuser
```

Сам проект и админ-панель по адресам:

```
http://127.0.0.1:8000

http://127.0.0.1:8000/admin
```

***
