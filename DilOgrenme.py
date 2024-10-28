kelimeler={}
print("Dil Öğrenme Programı")
print("1.Kelime Ekle")
print("2.Kelime Testi")
print("3.Cümle Kurma")
print("4.Çıkış")
while True:
    secim=input("Lütfen bir seçenek girin")
    if secim=="1":
        kelime=input("Lütfen eklemek istediğiniz kelimeyi girin")
        anlam=input("Lütfen kelimenin anlamını girin:").strip()
        kelimeler[kelime]=anlam
        print(f"{kelime} eklendi")
    elif secim=="2":
        if not kelimeler:
            print("Önce kelime eklemelisin")
            continue
        print("Kelime oyununa Hoş geldiniz")
        puan=0
        for kelime,anlam in kelimeler.items():
            cevap=input(f"{anlam}:").strip()

            if cevap.lower()==kelime.lower():
                print("Doğru")
                puan+=1
            else:
                print("Yanlış cevap girdin")

        print(f"Test tamamlandı")

    elif secim=="3":
        if not kelimeler:
            print("Önce kelime eklemelisin")
            continue
        print("Cümle Kurma Alıştırması")
        kelimelerListesi=list(kelimeler.keys())
        print("Aşağıdaki kelimelerle bir cümle oluşturun")
        print(",",join(kelimelerListesi))
        cumle=input("Oluşturduğunuz cümleyi girin")
        print(f"Oluşturduğunuz cümle : {cumle}")

    elif secim=="4":
        break
        
