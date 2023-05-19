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

satici_toplam_dict = {}
for key, value in magaza_dict.items():
    magaza_adi, satici_adi, satici_cinsi = key
    satis_tutari = value
    if satici_adi in satici_toplam_dict:
        satici_toplam_dict[satici_adi] += satis_tutari
    else:
        satici_toplam_dict[satici_adi] = satis_tutari

magaza_toplam_dict = {}
for key, value in magaza_dict.items():
    magaza_adi = key[0]
    satis_tutari = value
    if magaza_adi in magaza_toplam_dict:
        magaza_toplam_dict[magaza_adi] += satis_tutari
    else:
        magaza_toplam_dict[magaza_adi] = satis_tutari

magaza_toplam_dict = {}
for key, value in magaza_dict.items():
    magaza_adi = key[0]
    satis_tutari = value
    if magaza_adi in magaza_toplam_dict:
        magaza_toplam_dict[magaza_adi] += satis_tutari
    else:
        magaza_toplam_dict[magaza_adi] = satis_tutari


for i in range(len(magaza_dict)):
    print(nesneListesi[i])

print("\n")

for magaza_adi, toplam_satis in magaza_toplam_dict.items():
    print(f"{magaza_adi} mağazasının toplam satış tutarı: {toplam_satis}")

print("\n")
for satici_adi, toplam_satis in satici_toplam_dict.items():
    print(f"{satici_adi} satıcısının toplam satış tutarı: {toplam_satis}")