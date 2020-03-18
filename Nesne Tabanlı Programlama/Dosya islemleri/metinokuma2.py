class Dosya():
    
    def __init__(self):
         
        with open("metin.txt", "r" , encoding = "utf-8") as file:

            dosya_icerigi  = file.read()
            kelime = dosya_icerigi.split(" ")
            self.sade_kelime = list()

            for i in kelime:
                i = i.strip("\n")
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                
                self.sade_kelime.append(i)

    def kelime_kumele(self):
        kelimeler = set()
        
        for i in self.sade_kelime:
            kelimeler.add(i)

        for i in kelimeler:
            print(i)
            print("***************************")

    def kelime_say(self):
        kelime_sozlugu = dict()

        for i in self.sade_kelime:
            
            if (i in kelime_sozlugu):
                kelime_sozlugu[i] += 1

            else :
                kelime_sozlugu[i] = 1

        for kelime,sayi in kelime_sozlugu.items():
            
            print("{} kelimesi sözlüğün içinde {} defa geçiyor".format(kelime ,sayi))


dosya = Dosya()

dosya.kelime_kumele()


        

            


