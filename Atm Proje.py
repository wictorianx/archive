def encrypt(text):
    text = text[::-1]
    output = ""
    for i in text:
        for t in range(3):
            output += i
    return output
def decrypt(text):
    text = text[::-3]
    return(text)

def girisFunc():
    hesap = {}
    file = open ("hesap", "w+")
    print("***************AKP BANK***************")
    username = input("Yeni hesap oluşturmak için isminizi, Giriş yapmak için ID giriniz : ")
    try:
        username = int(username)
        username = encrypt(username)
        hesaplar = file.readlines()
        for (i) in hesaplar:
            if username in i.keys():
                password = input("Şifrenizi Giriniz : ")
                if decrypt(i.username) == password:
                    print("SİSTEME GİRŞİNİZ BAŞARI İLE SONUÇLANDI")
                    giris = True
            else:
                print("Username yanlış.Yeniden deneyiniz")


        #Giriş
    except:
        checker = True
        hesaplar = file.readline()
        if len(hesaplar) > 0:
            for (i) in hesaplar:
                if username in i.keys():
                    checker = False
        if checker:
            username = str(username)
            #Yeni Hesap
            password = input("Şifrenizi Giriniz : ")
            password = encrypt(password)
            hesap[username]=password
            file.write(hesap+"\n")
            id = len(file.readlines()-1)
            print("id niz : " + str(id))
        else:
            print("Username kullanıldığı için işleminiz gerçekleştirilemedi. Lütfen yeniden deneyiniz.")
girisFunc()