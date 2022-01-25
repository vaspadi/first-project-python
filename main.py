from replit import db

def add(key='', value=''):
  if (key == ''):
    key = input('Adding - Введите ключ: ')

  if (value == ''):
    value = input('Adding - Введите значение: ')

  db[key] = value
  
  print(f"Поле {key} было добавлено. Значение: {value}")

def delete(key=''):
  if (key == ''):
    key = input ('Removing - Введите ключ: ')

  del db[key]

  print(f"Поле {key} было удалено")

def dbLog():
  for key in db:
    print(f"db - {key}: {db[key]}")

dbLog()