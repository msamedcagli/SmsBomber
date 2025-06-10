2#Credits : https://github.com/tingirifistik/Enough-Reborn
import subprocess, sys, os

try:
    import requests, urllib3, uuid, colorama
except ImportError:
    print("Gerekli modüller indiriliyor...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "urllib3==1.26.13", "uuid==1.30", "colorama==0.3.9", "requests==2.31.0"])
finally:
    import concurrent.futures, json, os, random, requests, string, time, urllib, urllib3, uuid, colorama

from colorama import Fore, Style
from time import sleep
from os import system
from concurrent.futures import ThreadPoolExecutor, wait
import math

class SendSms():
    adet = 0
    
    def __init__(self, phone, mail):
        self.phone = str(phone)
        if len(mail) != 0:
            self.mail = mail
        else:
            self.mail = ''.join(choice(ascii_lowercase) for i in range(20))+"@gmail.com"
          
while 1:
    system("cls||clear")
    print("""{}

 Sms Api: {} 
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + "Enough Rev\n\n 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
        sleep(3)
        continue
    if menu in [1, 2]:
        # Thread sayısını al
        system("cls||clear")
        try:
            thread_count = int(input(Fore.LIGHTYELLOW_EX + "Thread sayısını giriniz [1-3000]: " + Fore.LIGHTGREEN_EX))
            if thread_count < 1 or thread_count > 3000:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Geçersiz thread sayısı!")
            sleep(3)
            continue

    if menu == 1:
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")

        # Thread'leri başlat
        service_chunks = split_services(servisler_sms, thread_count)
        with ThreadPoolExecutor(max_workers=thread_count) as executor:
            futures = []
            for tel_no in tel_liste:
                sms = SendSms(tel_no, mail)
                for chunk in service_chunks:
                    futures.append(
                        executor.submit(run_services, sms, chunk, kere, aralik)
                    )
            try:
                wait(futures)
            except KeyboardInterrupt:
                system("cls||clear")
                print("\nİşlem iptal edildi...")
                sleep(2)

    elif menu == 2:
        system("cls||clear")
        try:
           
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")

        send_sms = SendSms(tel_no, mail)
        service_chunks = split_services(servisler_sms, thread_count)
        
        try:
            while True:
                with ThreadPoolExecutor(max_workers=thread_count) as executor:
                    futures = []
                    for chunk in service_chunks:
                        for service in chunk:
                            futures.append(
                                executor.submit(getattr(send_sms, service))
                            )
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nMenüye Dönülüyor...")
            sleep(2)

    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
        break

