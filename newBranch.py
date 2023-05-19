    def __str__(self):
        toplamMagzaSatis = self.magaza_satis_tutar(self.__magaza_adi,self.__satici_adi)
        return f"Mağaza adı: {self.get_magaza_adi()}, Satıcı adı: {self.get_satici_adi()}, Satıcı cinsi: {self.get_satici_cinsi()}, Satış tutarı: {self.get_satis_tutari()}"