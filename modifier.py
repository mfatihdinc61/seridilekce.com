from flask import request
import string


class Hitap:

    def __init__(self):
        pass


    def isimci(self, isim):

        isim = isim.split()
        isim2 = []

        for word in isim:

            if word[0] == "i":
                word = word.replace("i", "İ", 1)

            for k in word[1:]:

                if k == "İ":
                    word = word.replace("İ", "i")

                if k == "Ş":
                    word = word.replace("Ş", "ş")

                if k == "Ğ":
                    word = word.replace("Ğ", "ğ")

                if k == "I":
                    word = word.replace("I", "ı")

            isim2.append(word)

        isim2 = " ".join(isim2)
        isim2 = string.capwords(isim2, sep=None)
        return isim2


    # def isimci(self, isim):
    #
    #     if isim[0] == "i":
    #         isim = isim.replace("i", "İ")
    #
    #     isim = isim.capitalize()
    #     return isim



    def soyisimci(self, soyisim):
        soyisim = soyisim.replace("i", "İ")
        soyisim = soyisim.upper()
        return soyisim

    def adres(self, adres):

        adres = adres.split()
        adres2 = []

        for word in adres:

            if word[0] == "i":
                word = word.replace("i", "İ", 1)

            for k in word[1:]:

                if k == "İ":
                    word = word.replace("İ", "i")

                if k == "Ş":
                    word = word.replace("Ş", "ş")

                if k == "Ğ":
                    word = word.replace("Ğ", "ğ")

                if k == "I":
                    word = word.replace("I", "ı")

            adres2.append(word)

        adres2 = " ".join(adres2)
        adres2 = string.capwords(adres2, sep=None)
        return adres2

    def ilce(self, ilce):

        for k in ilce[1:]:

            if k == "İ":
                ilce = ilce.replace("İ", "i")

            if k == "Ş":
                ilce = ilce.replace("Ş", "ş")

            if k == "Ğ":
                ilce = ilce.replace("Ğ", "ğ")

            if k == "I":
                ilce = ilce.replace("I", "ı")

        if ilce[0] == "i":
            ilce = ilce.replace("i", "İ", 1)


        ilce = ilce.capitalize()

        return ilce

    def il(self, il):
        il = il.replace("i", "İ")
        il = il.upper()
        return il

    # def teslimmakami(self, teslimmakami):
    #
    #     teslimmakami = request.form.get("")

    def teslimmakami(self, hitaben):

        hitap_up = hitaben.replace("İ", "i")
        hitap_up = hitap_up.replace("I", "ı")
        hitap_up = hitap_up.replace("U", "u")
        hitap_up = hitap_up.replace("Ü", "ü")

        last_letter = hitap_up[-1]

        na = ['a', 'ı', 'u']
        ne = ['i', 'ü']

        if [i for i in na if i == last_letter]:
            hitap_up = ''.join((hitaben, 'na'))
        elif [i for i in ne if i == last_letter]:
            hitap_up = ''.join((hitaben, 'ne'))


        hitap_up = hitap_up.replace("i", "İ")

        return hitap_up.upper()


    def ekci(self, ek):

        if ek[0] == "i":
            ek = ek.replace("i", "İ")

        ek = ek.capitalize()
        return ek


# a = Hitap()
# print(a.ilce("İşhakpaŞŞaİI"))