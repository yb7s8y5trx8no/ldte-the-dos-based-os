import time
import random
import string
from random import randint

gerceksifre = "lem2015"
animasyon = (" | ", " / ", "--", " \ ")
def baslangic_animasyonu():
    print("LDTE 4 Başlatılıyor...")
    for a in range(0,10):
        for i in animasyon:
            print(i, end='\r', flush=True)
            time.sleep(0.1)
    print("LDTE 4 Başlatıldı.")

baslangic_animasyonu()

time.sleep(3)

girilensifre = input("LÜTFEN ŞİFRENİZİ GİRİNİZ: ")
print("LÜTFEN BEKLEYİN...")
time.sleep(3)

time.sleep(1)
if girilensifre == gerceksifre:
    print("/////////////////////////////////////////////////////////////////////////////////////////////////////")
    print("LDTE 4 Başlatıldı. STARTUP.ELDPP dosyası kapatılıyor.")
    print("/////////////////////////////////////////////////////////////////////////////////////////////////////")
    while True:
        while True:
            c_devamikomut = input("C://")
            if c_devamikomut == "execute_calculater":
                print("Calculater.eldpp")
                sayi1 = int(input("İlk sayıyı giriniz: "))
                sayi2 = int(input("İkinci sayıyı giriniz: "))
                islem = input("İşleminiz (+ * - /):")
                
                if islem == "+":
                    print(sayi1 + sayi2)
                elif islem == "/":
                    print(sayi1 / sayi2)
                elif islem == "*":
                    print(sayi1 * sayi2)
                elif islem == "-":
                    print(sayi1 - sayi2)
            
            elif c_devamikomut == "sys_info":
                print("LDTE 4, sürüm 2")
                print("Edisyon: Pro")
                print("Kod ismi: Python 3.0")
                print("Ürün anahtarı: 8263r-3758f-5236v-2586d-9824e-8453l-5978p")
                
            elif c_devamikomut == "sys_update":
                print("Güncellemeler denetleniyor...")
                time.sleep(5)
                guncellemeyuklensinmi = input("Güncellemeler bulundu. İndirilip yüklensin mi (E/H)?")
                if guncellemeyuklensinmi == "E":
                    print("Güncelleme indiriliyor...")
                    time.sleep(30)
                    print("Güncelleme yükleniyor...")
                    time.sleep(15)
                    print("Güncelleme tamamlandı.")
                    print("Şimdi LDTE 4'ü yeniden başlatabilirsiniz.")
                else:
                    print("Güncelleme iptal edildi.")
            
            elif c_devamikomut == "sys_help":
                print("LDTE 4 Help")
                print("Merhaba. Bu LDTE 4.")
                print("Burada komutlar kullanılır.")
                print("İşte komutlar:")
                print("-----sys_update-----")
                print("Sistem güncellemeleri bununla denetlenip yüklenir.")
                print("-----sys_info-----")
                print("Sistem bilgileri bununla görüntülenir.")
                print("-----execute_calculator-----")
                print("Hesaplar bununla yapılır.")
                print("-----command_shutdown-----")
                print("Sistemi kapatır.")
                print("-----app_random_password_generator-----")
                print("Rastgele bir şifre oluşturur.")
                print("-----app_hang_man-----")
                print("Adam asmaca uygulamasını açar.")
                print("-----app_number_guess-----")
                print("Sayı tahmin uygulamasını açar.")
                print("-----sys_help-----")
                print("Burada yazanları tekrar okuyabilmenizi sağlar (Yani yardım programı).")
            
            elif c_devamikomut == "app_lem365":
                lem365app = input("Hangi lem 365 uygulamasını açmak istiyorsunuz?")
                if lem365app == "Lem Text":
                    print("Can't start Lem Text.")
                if lem365app == "Lem Office":
                    print("Can't start Lem Office.")
                if lem365app == "Lem Mail":
                    print("Can't start Lem Mail.")
            
            elif c_devamikomut == "sct -mode -3937d-8438g-7484r-4853h":
                c_devamikomut_secret_mode = input(" C://")
                if c_devamikomut_secret_mode == "app_secret_lem_defender":
                    secret_mode_defender_sifre = 30072011
                    secret_mode_defender_sifre_girilen = int(input("Sadece sayıların olduğu Lem Defender şifresini giriniz:  "))
                    if secret_mode_defender_sifre == secret_mode_defender_sifre_girilen:
                        print("Lem Defender'a hoş geldiniz.")
                        time.sleep(3)
                        print("Sistemde virüs taraması yapmak istiyoranız 1'e, virüs filtresini güncellemek istiyorsanız 2'ye, çıkmak istiyorsanız 3'e basınız.")
                        defender_secim = int(input())
                        if defender_secim == 1:
                            print("Virüs taraması başlatıldı.")
                            time.sleep(120)
                            print("Sistemde herhangi bir tehdit bulunmamıştır.")
                        if defender_secim == 2:
                            print("Filtre güncelleme işlemi başlatıldı.")
                            time.sleep(12)
                            print("Filtreler güncellendi.")
                        if defender_secim == 3:
                            print("Çıkış yapılıyor...")
                            time.sleep(2)
            
            elif c_devamikomut == "command_shutdown":
                print("Sistem kısa süre sonra kapanacak.")
                time.sleep(15)
                print("Kapatılıyor...")
                exit()
            
            elif c_devamikomut == "app_random_password_generator":
                random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                print("Oluşturulan şifre:", random_password)
                
            elif c_devamikomut == "app_number_guess":
                kolaySeviyeHak = 10
                zorSeviyeHak = 5


                # zorluk seviyesi yaz
                def zorluk_seviyesi():
                    seviye_tercihi = input("Oyun zorluğunu seçiniz. 'Kolay','Zor'\n").lower()
                    if seviye_tercihi == "kolay":
                        print("Oyunu kazanabilmek için 10 hakkın var!")
                        return kolaySeviyeHak
                    else:
                        print("Oyunu kazanabilmek için 5 hakkın var!")
                        return zorSeviyeHak


                def tahmin_oyunu():
                    print("Bilgisayar 1 ile 100 arasında bir sayıyı aklından tuttu.")
                    bilgisayar_tuttu = randint(1, 100)
                    devam_et = True
                    kalan_hak = zorluk_seviyesi()

                    while devam_et:
                        senin_tahminin = int(input("Bilgisayarın aklından tuttuğu sayı nedir?"))
                        if senin_tahminin > bilgisayar_tuttu:
                            print("Fazla attın, bir sonrakine küçük bir sayı seç!\n")
                            kalan_hak -= 1
                        elif senin_tahminin < bilgisayar_tuttu:
                            print("Ufak attın, bir dahakine büyük bir sayı seç!\n")
                            kalan_hak -= 1
                        else:
                            print("Tabrikler, kazandın!")
                            devam_et = False
                            yeni_oyun = input("Yeni bir oyun oynamaya ne dersin? 'Evet','Hayır'\n").lower()
                            if yeni_oyun == "evet":
                                tahmin_oyunu()
                            else:
                                devam_et = False

                        if kalan_hak == 0:
                            print("Hakkın bitti, oyunu kaybettin!")
                            devam_et = False
                            yeni_oyun = input("Yeni bir oyun oynamaya ne dersin? 'Evet','Hayır'\n").lower()
                            if yeni_oyun == "evet":
                                tahmin_oyunu()
                            else:
                                devam_et = False
                tahmin_oyunu()

            elif c_devamikomut == "app_hang_man":
                resim = ["""
                +---+
                |   |
                    |
                    |
                    |
                    |
                --------""","""
                +---+
                |   |
                O   |
                    |
                    |
                    |
                --------""","""
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                --------""","""
                +---+
                |   |
                O   |
                /|   |
                    |
                    |
                --------""","""
                +---+
                |   |
                O   |
                /|  |
                    |
                    |
                --------""","""
                +---+
                |   |
                O   |
                /|  |
                /    |
                    |
                --------""","""
                +---+
                |   |
                O   |
                /|  |
                /   |
                    |
                --------"""]

                while True:
                    print(("----->") + "Adam Asmaca Oyunu" + ("<-----"))
                    
                    kelime = random.choice(["python", "django", "terminal", "linux", "windows", "baskabirkod"])
                    adim = 0
                    tahmin = []
                
                    
                    while True:
                        print(resim[adim])
                        
                        for i, char in enumerate(kelime):
                            print(char if i in tahmin else "_"),
                            
                        cevap = input("nKelimeyi Tahmin Edin: ")
                        
                        if cevap == kelime:
                            print("Kazandınız!nn")
                            break
                        else:
                            while True:
                                rastgele = random.randint(0, len(kelime))
                                if not rastgele in tahmin:
                                    tahmin.append(rastgele)
                                    break
                            
                            adim += 1
                        
                        if adim >= len(resim):
                            print("Kaybettiniz!nn")
                            break
                        
                    if not "y" == input("Tekrar Oynamak İstermisiniz? (y/n): "):
                        break
                    
            elif c_devamikomut == "app_guess_the_unit":
                print("From Red Alert 2 Yuri's Revenge")
                time.sleep(0.5)
                print("G")
                time.sleep(0.2)
                print("u")
                time.sleep(0.2)
                print("e")
                time.sleep(0.2)
                print("s")
                time.sleep(0.2)
                print("s")
                time.sleep(0.2)
                print(" ")
                time.sleep(0.2)
                print("t")
                time.sleep(0.2)
                print("h")
                time.sleep(0.2)
                print("e")
                time.sleep(0.2)
                print(" ")
                time.sleep(0.2)
                print("u")
                time.sleep(0.2)
                print("n")
                time.sleep(0.2)
                print("i")
                time.sleep(0.2)
                print("t")
                time.sleep(0.2)
                print("Kodlayan: Can TEOMAN")
                time.sleep(1)
                seviye = int(input("Seviyenizi seçiniz (1,2). "))
                if seviye == 1:
                    bld_units_1 = random.choice(["Yuri battle lab", "Soviet flak cannon", "Allied construction yard", "Yuri floating disk", "Soviet flak truck", "Allied black eagle", "Yuri War factory", "Soviet ore refenery", "Allied MCV"])
                    print("Yuri battle lab, Soviet flak cannon, Allied construction yard, Yuri floating disk, Soviet flak truck, Allied black eagle, Yuri War factory, Soviet ore refenery, Allied MCV")
                    tahmin_bld_unit_1 = input("Tahmininiz: ")
                    if bld_units_1 == tahmin_bld_unit_1:
                        print("Tebrikler! Kazandınız!")
                    else:
                        print("Kaybettiniz.")
                if seviye == 2:
                    print("Yuri battle lab, Soviet flak cannon, Allied construction yard, Yuri floating disk, Soviet flak truck, Allied black eagle, Yuri War factory, Soviet ore refenery, Allied MCV, Yuri gattling cannon, Soviet flak trooper, Allied whether control device, Yuri yuri prime, Soviet ore miner, Allied chronominer")
                    bld_units_2 = random.choice(["Yuri battle lab", "Soviet flak cannon", "Allied construction yard", "Yuri floating disk", "Soviet flak truck", "Allied black eagle", "Yuri War factory", "Soviet ore refenery", "Allied MCV", "Yuri gattling cannon", "Soviet flak trooper", "Allied whether control device", "Yuri yuri prime", "Soviet ore miner", "Allied chronominer"])
                    tahmin_bld_unit_2 = input("Tahmininiz: ")
                    if tahmin_bld_unit_2 == bld_units_2:
                        print("Tebrikler! Kazandınız!")
                    else:
                        print("Kaybettiniz.")

            else:
                print("Bilinmeyen komut.")

        
    else:
        print("Giriş başarısız.")


