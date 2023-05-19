class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi):
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = 0

    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_magaza_adi(self):
        return self.__magaza_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari

    def get_satis_tutari(self):
        return self.__satis_tutari


    def magaza_satis_tutar(self, magaza_adi, satici_adi):
        magaza_toplam_dict = {}
        for key, value in magaza_dict.items():
            magaza_adi = key[0]
            satis_tutari = value
            if magaza_adi in magaza_toplam_dict:
                magaza_toplam_dict[magaza_adi] += satis_tutari
            else:
                magaza_toplam_dict[magaza_adi] = satis_tutari
        return magaza_toplam_dict[magaza_adi]

    def __str__(self):
        toplamMagzaSatis = self.magaza_satis_tutar(self.__magaza_adi,self.__satici_adi)
        return f"Mağaza adı: {self.get_magaza_adi()}, Satıcı adı: {self.get_satici_adi()}, Satıcı cinsi: {self.get_satici_cinsi()}, Satış tutarı: {self.get_satis_tutari()}"

magaza_dict = {}
nesneListesi = []

while True:

    magaza_adi = input("Mağaza adı giriniz (Çıkmak için h tuşuna basınız): ")
    if magaza_adi == "h":
        break
    satici_adi = input("Satıcı adı giriniz: ")
    satici_cinsi = input("Satıcı cinsi giriniz: ")
    satis_tutari = float(input("Satış tutarı giriniz: "))


    magaza = Magaza(magaza_adi, satici_adi, satici_cinsi)
    magaza.set_satis_tutari(satis_tutari)
    nesneListesi.append(magaza)
    key = (magaza_adi, satici_adi, satici_cinsi)
    if key in magaza_dict:
        magaza_dict[key] += satis_tutari
    else:
        magaza_dict[key] = satis_tutari



