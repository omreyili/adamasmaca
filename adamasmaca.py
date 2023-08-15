from random import randint
kelimeler = ["omer","faruk","yilmaz"]
bulunanharfler = []
can = 9
index = randint(0,3)
while True:
    for harf in kelimeler[index]:
        if harf in bulunanharfler:
            print(harf)
        else: 
            print("-")
    if len(bulunanharfler) == len(kelimeler[index]):
        print("kazandınız!")
        break
    girilenHarf = input("harf girin: ")
    if girilenHarf in kelimeler[index]:
        bulunanharfler.append(girilenHarf)
    elif can !=0:
        print("yanlış harf girdiniz.") 
        print("kalan canınız:",can)
        can = can - 1
    else:
        print("canınız bitti.")
        break