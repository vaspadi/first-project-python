from replit import db

def confirmContinue(operation):
  confirm = ''

  while confirm.lower() not in ('n', 'y'):
    confirm = input(f"{operation} - введите y или n - продолжить или закончить: ")

  return confirm == 'y'

def seedDb():
  confirm = confirmContinue('Test data generating')

  if (confirm == False): return

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
  confirm = confirmContinue('Adding')

  if (confirm == False): return

  if (key == ''):
    key = input('Adding - Введите ключ: ')

  if (value == ''):
    value = input('Adding - Введите значение: ')

  db[key] = value
  
  print(f"Поле {key} было добавлено. Значение: {value}")

def delete(key=None):

  if (key == None):
    confirm = confirmContinue('Removing')
    if (confirm == False): return

    key = input ('Removing - Введите ключ: ')

  if (isinstance(key, list)):
    for item in key:
      if hasattr(db, item): del db[item]

  else:
    if hasattr(db, key): del db[key]

  print(f"Поле {key} было удалено")

def dbLog():
  for key in db:
    print(f"db - {key}: {db[key]}")

def clearDb():
  for key in db:
    del db[key]

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

def createPerson(person = None, key = None):

  if (person != None and key != None): db[key] = person

  confirm = confirmContinue('Person creating')

  if (confirm == False): return

  dbKey = input('Введите ключ для db: ')
  firstName = input('Введите Имя: ')
  secondName = input('Введите Фамилию: ')
  number = input('Введите номер телефона: ')
  age = input('Введите возраст: ')
  isWorker = input('Работает ли он? (y/n): ')

  db[dbKey] = {
    'firstName': firstName,
    'secondName': secondName,
    'number': number,
    'age': age,
    'isWorker': isWorker == 'y',
  }

# print(findPersonBy('age', 20))

# delete(['person0', 'person1'])

# dbLog()
# 

clearDb()

seedDb()

createPerson()

delete()

dbLog()