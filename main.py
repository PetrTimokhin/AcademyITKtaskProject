# main.py
from fastapi import FastAPI, HTTPException, status
from typing import List, Dict, Optional  # Импортируем Optional
from models import User
from schemas import UserResponse, UserCreate, UserUpdate

app = FastAPI(
    title="Задание от ITK Academy",
    description="реализация простого REST API для управления пользователями",
    version="1.0.0",
)

# Имитация базы данных (словарь для хранения пользователей)
# Ключ - ID пользователя, значение - объект User
fake_db: Dict[int, User] = {}
next_user_id = 1


# --- Эндпойнты ---

# Изменения здесь: Добавлен параметр name_filter
@app.get("/users", response_model=List[UserResponse], summary="Получение всех пользователей с фильтром")
async def list_users(
        name_filter: Optional[str] = None):  # name_filter - query-параметр
    """
    Получает список всех пользователей, хранящихся в системе.

    Можно использовать необязательный параметр `name_filter` для фильтрации
    по частичному совпадению имени пользователя.

    Args:
        name_filter (Optional[str]): Строка для фильтрации списка пользователей по имени.
                                     Если указана, возвращаются только пользователи,
                                     чье имя содержит эту строку (регистр не учитывается).
                                     Если не указана, возвращаются все пользователи.
    """
    if name_filter:
        # Фильтрация по имени (регистронезависимая)
        filtered_users = [
            user for user in fake_db.values()
            if name_filter.lower() in user.name.lower()
        ]
        return [UserResponse(id=user.id, name=user.name, email=user.email) for
                user in filtered_users]
    else:
        # Возвращаем всех пользователей, если фильтр не указан
        return [UserResponse(id=user.id, name=user.name, email=user.email) for
                user in fake_db.values()]


@app.get("/users/{user_id}", response_model=UserResponse,
         summary="Получение пользователя по ID")
async def get_user(user_id: int):
    """
    Получает информацию о конкретном пользователе по его идентификатору.
    """
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    return UserResponse(id=user.id, name=user.name, email=user.email)


@app.post("/users", response_model=UserResponse,
          status_code=status.HTTP_201_CREATED, summary="Create a new user")
async def create_user(user_data: UserCreate):
    """
    Создает нового пользователя.
    Принимает имя и email пользователя.
    """
    global next_user_id
    new_user = User(id=next_user_id, name=user_data.name,
                    email=user_data.email)
    fake_db[next_user_id] = new_user
    next_user_id += 1
    return UserResponse(id=new_user.id, name=new_user.name,
                        email=new_user.email)


@app.put("/users/{user_id}", response_model=UserResponse,
         summary="Обновление данных пользователя")
async def update_user(user_id: int, user_data: UserUpdate):
    """
    Обновляет данные существующего пользователя по его идентификатору.
    Можно указать только те поля, которые нужно изменить (name, email).
    """
    user = fake_db.get(user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Пользователь не найден")

    if user_data.name is not None:
        user.name = user_data.name
    if user_data.email is not None:
        user.email = user_data.email

    fake_db[user_id] = user  # Обновляем в "базе"
    return UserResponse(id=user.id, name=user.name, email=user.email)


@app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT,
            summary="Удаление пользователя")
async def delete_user(user_id: int):
    """
    Удаляет пользователя по его идентификатору.
    """
    if user_id not in fake_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    del fake_db[user_id]
    # FastAPI автоматически вернет 204 No Content, если возвращаемое значение None
    return
