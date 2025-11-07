# Тестовое задание от ITK Academy
Этот проект демонстрирует реализацию простого REST API для управления
пользователями с использованием FastAPI и Pydantic.

## Структура папок проекта
AcademyITKtaskProject/ <br>
--main.py<br> 
--models.py<br>
--schemas.py<br>
--requirements.txt<br>
--README.md<br>

## Требования
* Python 3.7+

## Зависимости
    fastapi
    uvicorn[standard]
    pydantic[email]


## Запуск сервера
Создайте и активируйте виртуальное окружение (рекомендуется):

    bash
    
    python -m venv venv

Активация виртуального окружения:
#### Для Windows:
    venv\Scripts\activate
#### Для macOS/Linux:
    source venv/bin/activate
Установите необходимые зависимости: 

    bash
    
    pip install -r requirements.txt

Используйте uvicorn для запуска FastAPI приложения:

    bash
    
    uvicorn main:app --reload
main:app указывает на FastAPI приложение app в файле main.py.<br>
--reload включает автоматическую перезагрузку сервера при изменении кода.<br>
## Доступ к API
После запуска сервера API будет доступен по адресу:
    http://127.0.0.1:8000

## Документация Swagger UI
Автоматически сгенерированная документация API доступна по адресу: http://127.0.0.1:8000/docs

Вы можете использовать Swagger UI для интерактивного тестирования всех эндпойнтов:

GET /users: Получить список всех пользователей.<br><br>
Query Parameters:<br>
name_filter (string, optional):<br>
Фильтрует список пользователей по имени.
Возвращает пользователей, чье имя содержит указанную строку (регистр
не учитывается). Если параметр не указан, возвращаются все пользователи.<br><br>
GET /users/{user_id}:<br> Получить одного пользователя по ID.<br><br>
POST /users:<br> Создать нового пользователя.<br>
Тело запроса должно содержать name и email пользователя.<br><br>
PUT /users/{user_id}:<br> Обновить существующего пользователя по ID.
Тело запроса может содержать name и/или email для обновления.<br><br>
DELETE /users/{user_id}:<br> Удалить пользователя по ID.