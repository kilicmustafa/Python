class metinOkuma():
    
    def __init__(self):
        
        with open("metin.txt" ,"r" ,encoding = "utf-8") as file:

            dosya_icerigi = file.read()
            kelimeler = dosya_icerigi.split()
            self.sade_kelimeler = list()

            for i in kelimeler:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")

                self.sade_kelimeler.append(i)
                
    def kelimeAyırma(self):

        kelime_kumesi = set()

        for i in self.sade_kelimeler:
            kelime_kumesi.add(i)

        print("Tüm kelimeler ......")
        for i in kelime_kumesi:
            print(i)
            print("-----------------------")
    
    def kelimeFrekansi(self):
        kelime_sozlugu = dict()

        for i in self.sade_kelimeler:

            if (i in kelime_sozlugu):
                kelime_sozlugu[i] += 1
            
            else:
                kelime_sozlugu[i] = 1

        
        for kelime ,sayı in kelime_sozlugu.items():

            print("{} kelimesi {} defe geçiyor".format(kelime ,sayı))


oku = metinOkuma()
oku.kelimeAyırma()
oku.kelimeFrekansi()