from datetime import datetime, timezone
import arrow

base_url = 'https://petstore.swagger.io/v2'
headers1 = {'accept': 'application/json', 'Content-Type': 'application/json'}
headers2 = {'accept': 'application/json'}
headers3 = {'accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}

# ------------------------------------------------- for USER----------------------------------------

# Для создания нового пользователя

new_user = {
    "id": 0,
    "username": "SSSs",
    "firstName": "Petr",
    "lastName": "Sidorov",
    "email": "forsf2022@mail.ru",
    "password": "PaSsWoRd",
    "phone": "+7888",
    "userStatus": 0
}

# Для обновления данных пользователя

updated_user = {
    "id": 0,
    "username": "Seva",
    "firstName": "Savelij",
    "lastName": "Petrov",
    "email": "sfps@mail.ru",
    "password": "password",
    "phone": "+7999",
    "userStatus": 0
}

# Для создания пользователей списком

list_of_users_object = [
    {
        "id": 0,
        "username": "Ivan1",
        "firstName": "Ivan",
        "lastName": "Ivanov",
        "email": "ivan@mail.ru",
        "password": "ivan1",
        "phone": "+71111",
        "userStatus": 0
    },
    {
        "id": 0,
        "username": "Petr2",
        "firstName": "Petr",
        "lastName": "Sidorov",
        "email": "petr@mail.ru",
        "password": "petr2",
        "phone": "+72222",
        "userStatus": 0
    },
    {
        "id": 0,
        "username": "Foma3",
        "firstName": "Foma",
        "lastName": "Finskij",
        "email": "foma@mail.ru",
        "password": "foma3",
        "phone": "+73333",
        "userStatus": 0
    }
]

# Регистрация пользователя в системе

username = 'Vasja'
password = 'wordpass'

# -----------------------------------------------------------for PET-----------------------------

# Для добавления нового питомца
new_pet = {
    "id": 135,
    "category": {
        "id": 2,
        "name": "beast"
    },
    "name": "gorilla",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 13,
            "name": "horror"
        }
    ],
    "status": "available"
}

# Для изменения в данных о существующем питомце

update_new_pet = {
    "id": 135,
    "category": {
        "id": 2,
        "name": "string"
    },
    "name": "Kong",
    "photoUrls": [
        "string"
    ],
    "tags": [
        {
            "id": 3,
            "name": "string"
        }
    ],
    "status": "sold"
}

# Обновление данных о питомце с помощью данных формы

update_name = 'Monja'
update_status = 'new_status'

# ------------------------------------------------------for STORE-------------------------------------

# Оформить заказ на питомца
order = {
  "id": 2,
  "petId": 135,
  "quantity": 1,
  "shipDate": str(arrow.now()),
  "status": "placed",
  "complete": True
}