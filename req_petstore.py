import requests
import json
from config import new_user, base_url, updated_user, headers1, headers2, headers3, list_of_users_object, username, \
    password, new_pet, update_new_pet, update_name, update_status, order
from pprint import pprint

# --------------------------------- USER - ----------------------------------------------------
# Logs user into the system
"' Регистрация пользователя в системе"''

res = requests.get(f'{base_url}/user/login?username={username}&password={password}', headers=headers2)

print('Code (Logs user into the system) = ', res.status_code)
print('Response body (Logs user into the system):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Logs user into the system):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Create user
"' Создали нового пользователя"''

info_js = json.dumps(new_user, ensure_ascii=False)

res = requests.post(f'{base_url}/user', headers=headers1, data=info_js)

print('Code (Create user) = ', res.status_code)
print('Response body (Create user):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Create user):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

#

# Updated user
"'Внесли изменения '"

username = new_user["username"]
info_js = json.dumps(updated_user, ensure_ascii=False)

res = requests.put(f'{base_url}/user/{username}', headers=headers1, data=info_js)

print('Code (Updated user)= ', res.status_code)
print('Response body (Updated user):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Updated user):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Get  user by user name
"'Нашли user по user name'"

username = updated_user["username"]
res = requests.get(f'{base_url}/user/{username}', headers=headers2)

print('Code (Get  user by user name)= ', res.status_code)
print('Response body (Get  user by user name):')
pprint(res.json(), indent=10)
print('Response headers (Get  user by user name):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Creates list of users with given input array
"'Создание пользователей списком 1'"

info_js = json.dumps(list_of_users_object, ensure_ascii=False)
res = requests.post(f'{base_url}/user/createWithArray', headers=headers1, data=info_js)

print('Code ((/user/createWithArray)Creates list of users with given input array)= ', res.status_code)
print('Response body ((/user/createWithArray)Creates list of users with given input array):')
pprint(res.json(), width=40, indent=10)
print('Response headers ((/user/createWithArray)Creates list of users with given input array):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Creates list of users with given input array 2
"'Создание пользователей списком2(в чем разница???)'"

info_js = json.dumps(list_of_users_object, ensure_ascii=False)
res = requests.post(f'{base_url}/user/createWithList', headers=headers1, data=info_js)

print('Code ((/user/createWithList)Creates list of users with given input array)= ', res.status_code)
print('Response body ((/user/createWithList)Creates list of users with given input array):')
pprint(res.json(), width=40, indent=10)
print('Response headers ((/user/createWithList)Creates list of users with given input array):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Delete user
"'Удалили user по user name'"

username = updated_user["username"]
res = requests.delete(f'{base_url}/user/{username}', headers=headers2)

print('Code (Delete user)= ', res.status_code)
print('Response body (Delete user):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Delete user):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Logs out current logged in user session
"' Выход из текущего сеанса пользователя, вошедшего в систему"''

res = requests.get(f'{base_url}/user/logout', headers=headers2)

print('Code (Logs out current logged in user session) = ', res.status_code)
print('Response body (Logs out current logged in user session):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Logs out current logged in user session):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# ------------------------------------------------ PET -----------------------------------------------------

# Add a new pet to the store
"' Добавили нового питомца"''

info_js = json.dumps(new_pet, ensure_ascii=False)

res = requests.post(f'{base_url}/pet', headers=headers1, data=info_js)

print('Code (Add a new pet to the store) = ', res.status_code)
print('Response body (Add a new pet to the store):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Add a new pet to the store):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Upload an image
"' Добавили фото нового питомца"''

id_new_pet = res.json()['id']
pet_photo = 'Bigzver.jpg'
files = {'file': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')}

res = requests.post(f'{base_url}/pet/{id_new_pet}/uploadImage', headers=headers2, files=files)

print('Code (Upload an image) = ', res.status_code)
print('Response body (Upload an image):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Upload an image):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Update an existing pet
"' Изменение в данных о новом питомце'"

info_js = json.dumps(update_new_pet, ensure_ascii=False)

res = requests.put(f'{base_url}/pet', headers=headers1, data=info_js)

print('Code (Update an existing pet) = ', res.status_code)
print('Response body (Update an existing pet):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Update an existing pet):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Finds pets by status
# "'Находим питомцев по статусу'"

status = 'pending'
res = requests.get(f'{base_url}/pet/findByStatus?status={status}', headers=headers2)

print('Code (Finds pets by status)= ', res.status_code)
print('Response body (Finds pets by status):')
pprint(res.json(), indent=10)
print('Response headers (Finds pets by status):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Find pet by ID
# "'Находим питомца по ID'"

res = requests.get(f'{base_url}/pet/{id_new_pet}', headers=headers2)

print('Code (Find pet by ID)= ', res.status_code)
print('Response body (Find pet by ID):')
pprint(res.json(), indent=10)
print('Response headers (Find pet by ID):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Updates a pet in the store with form data
"'Обновление данных о питомце с помощью данных формы'"

info_js = f'name={update_name}&status={update_status}'

res = requests.post(f'{base_url}/pet/{id_new_pet}', headers=headers3, data=info_js)

print('Code (Updates a pet in the store with form data)= ', res.status_code)
print('Response body (Updates a pet in the store with form data):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Updates a pet in the store with form data):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Delete a pet
"'Удаляем питомца'"

res = requests.delete(f'{base_url}/pet/{id_new_pet}', headers=headers2)

print('Code (Delete a pet)= ', res.status_code)
print('Response body (Delete a pet):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Delete a pet):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# ------------------------------------------------ STORE -----------------------------------------------------

# Place an order for a pet
"'Оформить заказ на питомца'"

info_js = json.dumps(order, ensure_ascii=False)

res = requests.post(f'{base_url}/store/order', headers=headers1, data=info_js)

print('Code (Place an order for a pet)= ', res.status_code)
print('Response body (Place an order for a pet):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Place an order for a pet):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Find purchase order by ID
"'Найти заказ на покупку по id'"

res = requests.get(f'{base_url}/store/order/{res.json()["id"]}', headers=headers2)

print('Code (Find purchase order by id)= ', res.status_code)
print('Response body (Find purchase order by id):')
pprint(res.json(), indent=10)
print('Response headers (Find purchase order by id):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Delete purchase order by ID
"'Найти заказ на покупку по id'"

res = requests.delete(f'{base_url}/store/order/{res.json()["id"]}', headers=headers2)

print('Code (Delete purchase order by ID)= ', res.status_code)
print('Response body (Delete purchase order by ID):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Delete purchase order by ID):')
pprint(dict(res.headers), indent=10)

print('-------------------------------------------------------------')

# Returns pet inventories by status
"' Возвращает количество питомцев по статусу'"

res = requests.get(f'{base_url}/store/inventory', headers=headers2)

print('Code (Returns pet inventories by status)= ', res.status_code)
print('Response body (Returns pet inventories by status):')
pprint(res.json(), width=40, indent=10)
print('Response headers (Returns pet inventories by status):')
pprint(dict(res.headers), indent=10)
