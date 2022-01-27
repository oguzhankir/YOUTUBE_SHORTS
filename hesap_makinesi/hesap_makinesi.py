#işlemlerimizi tanımlayalım

def toplama(sayı1, sayı2):
    return sayı1 + sayı2

def cikarma(sayı1, sayı2):
    return sayı1 - sayı2

def carpma(sayı1, sayı2):
    return sayı1 * sayı2

def bolme(sayı1, sayı2):
    return sayı1 / sayı2

#input alalım

print("Yapacağınız işlemi seçin \n",
        "1. Toplama \n",
        "2. Çıkarma \n",
        "3. Çarpma \n",
        "4. Bolme"
)

secim = int(input("seçtiğiniz işlemi 1,2,3,4" \
                    "olacak şekilde giriniz: "))

sayı1 = int(input("ilk sayıyı giriniz: "))
sayı2 = int(input("ikinci sayıyı giriniz: "))

if secim ==1:
    print(sayı1, "+", sayı2, "=", toplama(sayı1, sayı2))

if secim ==2:
    print(sayı1, "-", sayı2, "=", cikarma(sayı1, sayı2))

if secim ==3:
    print(sayı1, "*", sayı2, "=", carpma(sayı1, sayı2))

if secim ==4:
    print(sayı1, "/", sayı2, "=", bolme(sayı1, sayı2))