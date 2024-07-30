### Тестовое задание для junior разработчика

Необходимо создать web-приложение, которое будет хранить и обрабатывать информацию по сотрудникам компании X.
Приложение должно обеспечивать возможность:

* Создавать, просматривать, редактировать и ликвидировать(выводить из работы, но не удалять)
структурные подразделения компании, такие как отделы, службы, департаменты и пр.
(будет плюсом если это будет организовано в иерархическую структуру).
Для описания подразделения достаточно использовать его 4-значный код, полное наименование, аббревиатуру,
дату создания и ликвидации.<br>


* Просматривать информацию о работниках, добавлять новых и редактировать имеющихся.
Описание одного работника включает: табельный номер, ФИО, пол, дату рождения, дату приема/перевода-прибытия,
дату увольнения/перевода-выбытия, подразделение, должность, телефон, электронную почту, и фотографию.
Если фото отсутствует, то должен отображаться силуэт человека М/Ж. На странице информации о сотруднике пользователю
необходимо отображать возраст работника и сколько полных лет работает в компании на момент просмотра.<br>


* Принимать/переводить/увольнять сотрудников.<br>


* Формировать списочный отчет по принятым/переведенным/уволенным за установленный период.


В качестве БД настоятельно рекомендуется
использовать **PostgreSQL**.

---

### Инструкция по запуску проекта.

Версия python 3.10.1, скачать можно с официального сайта: https://www.python.org/downloads/

Клонируйте проект в локальную папку или на удалённый сервер: --> [инструкция](https://docs.github.com/ru/repositories/creating-and-managing-repositories/cloning-a-repository)

Проверяем версию python, , вам может понадобиться прописывать версию *python3*
```bash
python --version
```
Устанавливаем виртуальную среду из папки проекта
```bash
python -m venv venv
```
Активация виртуальной среды
```bash
.\venv\Scripts\activate
```
Устанавливаем зависимости из файла requirements.txt
```bash
python -m pip install -r requirements.txt
```
Проверяем список установленных библиотек
```bash
pip list
```
В файле employees_records/settings.py вносим данные своей базы
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_service',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'USER': '',
        'PASSWORD': ''
    }
}
```
Создаём миграции
```bash
python manage.py makemigrations
```
Применяем их
```bash
python manage.py migrate
```
Запускаем сервер
```bash
python manage.py runserver
```
Для регистрации суперпользователя используется следующая команда (в данном проекте не обязательно):
```bash
python manage.py createsuperuser
```
Для входа в админ-панель откройте ссылку /admin (например http://127.0.0.1:8000/admin) и введите логин и пароль вашего нового суперпользователя (вас перенаправят на login-страницу и потом обратно на /admin после ввода всех деталей).