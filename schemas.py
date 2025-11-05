from typing import Optional
from pydantic import BaseModel, EmailStr

# Схема для представления пользователя (для GET и LIST)
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr

    # class Config:
    #     orm_mode = True  # Позволяет Pydantic работать с моделями, которые имеют атрибуты, а не только поля BaseModel

# Схема для создания нового пользователя (для POST)
class UserCreate(BaseModel):
    name: str
    email: EmailStr

# Схема для обновления существующего пользователя (для PUT)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
