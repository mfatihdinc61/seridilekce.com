import math
import textwrap
import time
from datetime import date, timedelta, datetime
import os
from fpdf import fpdf, FPDF
from modifier import Hitap
from random import *
from string import *
ayarci = Hitap()


class thedilekce():

    def __init__(self, isim, soyisim, adres, ilce, il, teslimmakami, tarih, metin, radioVal=None, telno=None,
                 eposta=None, ek1=None,
                 ek2=None, ek3=None, ek4=None, ek5=None):

        self.d0 = None

        self.ek1 = ek1.strip()
        self.ek2 = ek2.strip()
        self.ek3 = ek3.strip()
        self.ek4 = ek4.strip()
        self.ek5 = ek5.strip()

        self.metin = metin.strip()
        self.tarih = tarih
        self.teslimmakami = teslimmakami
        self.eposta = eposta.strip()
        self.telno = telno.strip()
        self.il = il
        self.ilce = ilce
        self.adres = adres
        self.soyisim = soyisim
        self.isim = isim
        self.radioVal = radioVal

    def pdfolustur(self):
        
        
        def generate_password(length=25):
            
            characters = ascii_letters + digits
            password = ''.join(choice(characters) for _ in range(length))
            return password

            # Example usage:
        pdf_name = generate_password()
        
        
        self.d0 = pdf_name
        thefilename = f"{self.d0}.pdf"
        

        global page1_content, page2_content
        self.teslimmakami = ayarci.teslimmakami(self.teslimmakami).strip()
        self.il = ayarci.il(self.il).strip()
        self.ilce = ayarci.ilce(self.ilce).strip()
        self.adres = ayarci.adres(self.adres).strip()
        self.soyisim = ayarci.soyisimci(self.soyisim).strip()
        self.isim = ayarci.isimci(self.isim).strip()

        if self.ek1:
            self.ek1 = ayarci.ekci(self.ek1)

        if self.ek2:
            self.ek2 = ayarci.ekci(self.ek2)

        if self.ek3:
            self.ek3 = ayarci.ekci(self.ek3)

        if self.ek4:
            self.ek4 = ayarci.ekci(self.ek4)

        if self.ek5:
            self.ek5 = ayarci.ekci(self.ek5)

        thedilekce = FPDF(orientation='P', unit='cm', format='A4')
        thedilekce.set_auto_page_break(0)

        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'tt2.ttf')
        thedilekce.add_font('turkce-font', '', my_file, uni=True)

        thedilekce.set_margins(2.5, 2.5, 2.5)
        thedilekce.set_font('turkce-font', style='', size=12)

        thedilekce.add_page()

        """inputlar"""

        isim_soyisim = f"{ayarci.isimci(isim=self.isim)} {self.soyisim}"

        if self.telno and self.eposta:
            tam_adres = f"{self.adres}\n{self.ilce}/{self.il}\nTelefon: {self.telno}\n{self.eposta}"

        elif self.telno:
            tam_adres = f"{self.adres}\n{self.ilce}/{self.il}\nTelefon: {self.telno}"

        elif self.eposta:
            tam_adres = f"{self.adres}\n{self.ilce}/{self.il}\n{self.eposta}"

        else:
            tam_adres = f"{self.adres}\n{self.ilce}/{self.il}"

        self.metin = self.metin.strip()
        self.metin = textwrap.indent(text=self.metin, prefix='             ')

        arz = "Gereğini saygılarımla arz ederim."

        """radio val part"""
        if self.radioVal == "1":
            arz = "Gereğini saygılarımla arz ederim."

        elif self.radioVal == "2":
            arz = "Takdirlerinize arz ederim."

        elif self.radioVal == "3":
            arz = "Bilgilerinize arz ederim."


        # threshold hesapları

        numOfLinesInPetition = len(self.metin) / 90
        hamAdresPoint = math.ceil(len(self.adres.split()) / 24)

        mailPoint = 0
        telefonPoint = 0

        if self.eposta:
            mailPoint = 1
        if self.telno:
            telefonPoint = 1

        ek1Point = 0
        ek2Point = 0
        ek3Point = 0
        ek4Point = 0
        ek5Point = 0

        if self.ek1:
            ek1Point = 2
            if self.ek2:
                ek2Point = 1
                if self.ek3:
                    ek3Point = 1
                    if self.ek4:
                        ek4Point = 1
                        if self.ek5:
                            ek5Point = 1

        total = numOfLinesInPetition * 0.5 + 1.1
        baslama_noktasi = 0.7 * ((29.7 - total) / 2)

        ekPuan = ek1Point + ek2Point + ek3Point + ek4Point + ek5Point

        finalPointForAdress = ek1Point + ek2Point + ek3Point + ek4Point + ek5Point + mailPoint + telefonPoint + hamAdresPoint*1.5
        theDeterminer = numOfLinesInPetition * 0.5 + finalPointForAdress * 0.5 + baslama_noktasi + 5

        setYForEk = -(ekPuan*0.5+1.75)
        setYForAdress = -(finalPointForAdress*0.6+3)


        the_number = len(self.metin)
        wordsInPetition = self.metin.split()

        if theDeterminer < 27.5:

            satir_sayisi = the_number / 92
            satir_sayisi = math.ceil(satir_sayisi)
            total = satir_sayisi * 0.5 + 1.1
            baslama_noktasi = 0.7 * ((29.7 - total) / 2)

            if baslama_noktasi < 3.5:
                baslama_noktasi = 3.5

            print(len(self.adres))

            hamAdresPoint = math.ceil(len(self.adres) / 24)
            print(f"ham adres point: {hamAdresPoint}")

            """ tarih """
            thedilekce.set_xy(-5, 1.5)
            thedilekce.cell(w=16, h=1, txt=self.tarih)

            """ hitap """
            thedilekce.set_y(baslama_noktasi)
            thedilekce.multi_cell(w=16, h=0.5, txt=self.teslimmakami, align='C')

            """BOŞLUK"""
            thedilekce.multi_cell(w=16, h=0.6, txt="", align='C')

            """ metin """
            thedilekce.multi_cell(w=16, h=0.5, txt=self.metin)

            """ arz cümlesi"""
            thedilekce.set_x(3.95)
            thedilekce.multi_cell(w=16, h=0.5, txt=arz)

            """boşluk"""
            thedilekce.multi_cell(w=12, h=1.2, txt="")

            """ isim-soyisim """
            thedilekce.set_x(-9)
            thedilekce.multi_cell(w=12, h=0.5, txt=isim_soyisim)

            """tam adres"""
            thedilekce.set_y(setYForAdress)
            thedilekce.multi_cell(w=6, h=0.5, txt="Adres:")

            """tam adres-2"""
            thedilekce.set_xy(3.75, setYForAdress)
            thedilekce.multi_cell(w=6, h=0.5, txt=tam_adres, align='L')
            self.tam_adres = tam_adres


            """ekler ek-1"""
            if self.ek1:
                thedilekce.set_y(setYForEk)
                thedilekce.multi_cell(w=0, h=0.5, txt="Ekler: ")
                thedilekce.set_xy(3.75, setYForEk)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"1. {self.ek1}")

            """ek-2"""
            if self.ek2:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"2. {self.ek2}")

            """ek-3"""
            if self.ek3:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"3. {self.ek3}")

            """ek-4"""
            if self.ek4:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"4. {self.ek4}")

            """ek-5"""
            if self.ek5:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"5. {self.ek5}")

            # self.d0 = datetime.now().timestamp()
            # thefilename = f"{self.d0}.pdf"

            # d = f"static/{self.d0}.pdf"
            # pdfarrival = os.path.dirname(os.path.abspath(__file__))
            """değişecek kısım pythonanywhere için"""
            # d = f"/home/falan/filan/static/pdfs/{self.d0}.pdf"

            d = f"/home/falan/filan/static/pdfs/{self.d0}.pdf"

            thedilekce.output(d, 'F')
            return thefilename

        else:

            try:
                thresholdCharacter = self.metin[3700]
                thresholdNumber = 3700
                i = 0

                while thresholdCharacter != ' ':
                    thresholdCharacter = self.metin[3700 + i]
                    thresholdNumber = 3700 + i
                    i = i + 1

                page1_content = self.metin[:thresholdNumber]
                page2_content = self.metin[thresholdNumber:]

                adSoyadFlag = 0
                arzFlag = 0

                if len(page1_content) < 3700:

                    adSoyadFlag = 1
                    arzFlag = 1

            except:
                page1_content = self.metin[:len(self.metin)]
                page2_content = ""

                adSoyadFlag = 1
                arzFlag = 1

            satir_sayisi = len(page1_content) / 92
            satir_sayisi = math.ceil(satir_sayisi)

            total = satir_sayisi * 0.5 + 1.1
            baslama_noktasi = 0.7 * ((29.7 - total) / 2)

            # print(math.ceil(satir_sayisi))

            """sayfa numarası ilk sayfa"""
            thedilekce.set_xy(10.5, -1)
            thedilekce.cell(w=16, h=1, txt="1")

            """ tarih """
            thedilekce.set_xy(-5, 1.5)
            thedilekce.cell(w=16, h=1, txt=self.tarih)

            """ hitap """
            thedilekce.set_y(baslama_noktasi)
            thedilekce.multi_cell(w=16, h=0.5, txt=self.teslimmakami, align='C')

            """BOŞLUK"""
            thedilekce.multi_cell(w=16, h=0.6, txt="", align='C')

            """ metin """
            # thedilekce.set_x(4)
            thedilekce.multi_cell(w=16, h=0.5, txt=page1_content)
            if arzFlag:
                thedilekce.set_x(3.95)
                thedilekce.multi_cell(w=16, h=0.5, txt=arz)

                "boşluk"
                thedilekce.multi_cell(w=16, h=1.6, txt="", align='C')

                "arz cümlesi"
                thedilekce.set_x(-9)
                thedilekce.multi_cell(w=12, h=0.5, txt=isim_soyisim)

            # ikinci sayfa
            thedilekce.add_page()

            """sayfa numarası ikinci sayfa"""
            thedilekce.set_xy(10.5, -1)
            thedilekce.cell(w=16, h=1, txt="2")

            thedilekce.set_xy(2.5, 2.5)
            thedilekce.multi_cell(w=16, h=0.5, txt=page2_content)

            page2LineNumber = len(page2_content) / 92
            page2distance = page2LineNumber * 0.5 + 3.5

            """ arz cümlesi """
            if not arzFlag:
                thedilekce.set_x(3.95)
                thedilekce.multi_cell(w=16, h=0.5, txt=arz)

            """ isim-soyisim """
            if not adSoyadFlag:
                "boşluk"
                thedilekce.multi_cell(w=16, h=1.6, txt="", align='C')
                thedilekce.set_x(-9)
                thedilekce.multi_cell(w=12, h=0.5, txt=isim_soyisim)


            """tam adres"""
            thedilekce.set_y(setYForAdress)
            thedilekce.multi_cell(w=6, h=0.5, txt="Adres:")

            """tam adres-2"""
            thedilekce.set_xy(3.75, setYForAdress)
            thedilekce.multi_cell(w=8, h=0.5, txt=tam_adres, align='L')
            self.tam_adres = tam_adres


            """ekler ek-1"""
            if self.ek1:
                thedilekce.set_y(setYForEk)
                thedilekce.multi_cell(w=0, h=0.5, txt="Ekler: ")
                thedilekce.set_xy(3.75, setYForEk)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"1. {self.ek1}")

            """ek-2"""
            if self.ek2:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"2. {self.ek2}")

            """ek-3"""
            if self.ek3:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"3. {self.ek3}")

            """ek-4"""
            if self.ek4:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"4. {self.ek4}")

            """ek-5"""
            if self.ek5:
                thedilekce.set_x(3.75)
                thedilekce.multi_cell(w=0, h=0.5, txt=f"5. {self.ek5}")

            # self.d0 = datetime.now().timestamp()
            # thefilename = f"{self.d0}.pdf"

            d = f"/home/falan/filan/static/pdffiles/{self.d0}.pdf"

            return thefilename



# thetext = "fatih universitesi"

# thedilekce(isim="ali", soyisim="çevik", adres="başal mah. 4. etap 2.kısım", ilce="sürmene", il="trabzon",
#            telno="05350611385", eposta="mfatihdinc61@gmail.com", teslimmakami="Ankara Valiliği", tarih="29.05.2023",
#            metin="30 günlük iznimi kullanmak istiyorum, ilgililerin bilgilerine").pdfolustur()

"""p-1: latin-1 problemi, üniversite yazamıyoruz, satır farklarının oluşturulması"""
"""p-2: satırlar arası boşluk ne olmalı belli değil, h=0.6 cm kullandık"""
"""p-3: indentin 1.5 cm ayarlanması """
"""p-4: birden çok paragrafla yazılma durumu"""
"""p-5: **ikinci sayfa ekleme**"""
"""p-6: ek numarasını düzgün yere ekleme + sayfa numarası"""
"""p-7: paragrafların ayrılması"""
"""p-8: metin içinde "-" kullanılması"""
"""p-9: hitap kurumunun son harfinin farklı bitmesi"""
"""p-10: harf sınırı koyulması"""
"""p-11: adresin doğru boşlukla düşmemesi"""
"""p-12: serverın fail etmesi"""
"""p-13: ek eklede sayfanın sarsılması"""
"""p-14: butonun bazı durumlarda çalışmaması"""
"""p-15: imza atmayı unutmayın iletisi """
