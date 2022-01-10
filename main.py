from replit import db

def add(key='', value=''):
  title = 'Добавление -'
  
  if (key == ''):
    key = input(title + ' Введите ключ: ')

  if (value == ''):
    value = input(title + ' Введите значение: ')

  db[key] = value
  
  print(title + ' success')

def delete(key=''):
  title = 'Удаление -'
  if (key == ''):
    key = input (title + ' Введите ключ: ')

  del db[key]

  print(title + ' success')