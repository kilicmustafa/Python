"""Bu projede ise 4 tane sınıfı oluşturun.

Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.

Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.

Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.

At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin. """

import time as t


class Hayvan():
    def  __init__(self ,ad ,tur ,cinsiyet ,yas):
        self.ad = ad
        self.tur = tur 
        self.cinsiyet = cinsiyet
        self.yas = yas

    def __str__():
        return "Burası Hayvanların Ortak özelliklerini barındırıyor"

class Köpek(Hayvan):
    def __init__(self ,kuduzmu ):
        super().__init__(ad ,tur ,cinsiyet ,yas)
        self.kuduzmu = kuduzmu

    def __str__():
        return "Burası Kopekler sınıfıdır Hayvan sınıfından miras almıştır"

    def atYasDeğis(self,yeni_yas):
        print("Yas Değisiliyor ...")
        t.sleep(1)
        self.yas = yeni_yas
    
        
class Kuş(Hayvan):
    def __init__(self ,kanatBoyutu):
        super().__init__(ad ,tur ,cinsiyet ,yas)
        self.kanatBoyutu =kanatBoyutu
    def __str__():
        return "Burası kuş sınıfıdır ve Hayvan sınıfından miras almıştır"
