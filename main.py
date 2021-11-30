# class Info:
#   def __init__(self):
#     self.PVN = 21
#     self.darbaSamaksa = 15
#     self.user = {}

#   def ievaditUserInfo(self):
#     props = ['klient', 'veltijums', 'augstums', 'garums']

#     for prop in props:
#       self.user[prop] = input(f'Ievadi ${prop}:')

# class Rekins:
#   def __init__(self, info):
#     self.info = info

#   def izdrukat(self):
#     for attr, value in info.user.__dict__.items():
#       print(f'{attr}: {value}')

#   def changeProps(self):
#     self.izdrukat()

#     for attr, value in self.__dict__.items():
#       self[attr] = input(f'Новое значение для {attr}:')

# info = Info()
# info.ievaditUserInfo()

# rekins = Rekins(info)

# rekins.izdrukat()
klient = 'pavel'

def saveDates():
  import csv

  with open (f'{klient}.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['name', ' veltijums', 'izmeri', 'cena'])
    print('Saved')

saveDates()