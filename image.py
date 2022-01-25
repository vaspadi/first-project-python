class Ballite:
  dekoracijas = ['cekuri', 'bumbinas']
  ciemini = ''
  ediens = ['kaposti', 'brokali']
  tematika = '80tie gadi'
  vel_davanas = ['telefons', 'konfectes']

  def pirkumi(self):
    for item in self.dekoracijas:
      print('dekoracija: ', item)

    for item in self.ediens:
      print('ediens: ', item)

  def davanas(self):
    davanas = self.vel_davanas

    for davana in davanas:
      print('davana: ', davana)


elem = Ballite()

elem.pirkumi()
elem.davanas()
print('tematika: ', elem.tematika)
print('ciemini: ', elem.ciemini)