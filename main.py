from replit import db

def seedDb():
# Set test data id db
  for index in range(5):
    db[f"person{index}"] = {
      'firstName': f"Name{index}",
      'secondName': f"SecondName{index}",
      'number': f"+37{index} 28282828",
      'age': 18 + index,
      'isWorker': index % 2 == 0,
    }

def add(key='', value=''):
  if (key == ''):
    key = input('Adding - Введите ключ: ')

  if (value == ''):
    value = input('Adding - Введите значение: ')

  db[key] = value
  
  print(f"Поле {key} было добавлено. Значение: {value}")

def delete(key=None):
  if (key == None):
    key = input ('Removing - Введите ключ: ')

  if (isinstance(key, list)):
    for item in key:
      del db[item]

  else:
    del db[key]

  print(f"Поле {key} было удалено")

def dbLog():
  for key in db:
    print(f"db - {key}: {db[key]}")

def getKeyByValue(value = ''):
  if (value == ''):
    value = input('Key getting - Введите значение')

  for key in db:
    if (value == db[key]):
      return key

def findPersonBy(key = '', value = None):
  if (key == ''):
    key = input('Finding - Введите ключ: ')

  if (value == None):
    value = input(f"Finding - Введите значение, для ключа {key}: ")

  result = []

  for dbKey in db:
    if (value == db[dbKey][key]):
      result.append(db[dbKey])
  
  return result

print(findPersonBy('age', 20))