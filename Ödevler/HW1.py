liste=["elma","armut","kalem","kitap"]
liste1=liste[0:2]
liste2=liste[2:5]
print(liste2+liste1)

sayi=int(input("Tek basamaklı bir tamsayı giriniz:"))
try:
    if sayi>=0:
      print("Çift Sayılar:")
      for i in range (sayi):
        if i%2==0:
          print(i)
except:
  print("Sayı Giriniz:")
