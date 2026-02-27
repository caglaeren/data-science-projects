# Veri Simülasyonu 

#np.random ile müşteri ID, ürün, şehir, satış tutarı, ay bilgisi üret
#bilerek NaN değerler koy, uç değerler üret
import numpy as np
import pandas as pd
#1000 adet veri ürettik
def generate_sales_data(size=1000):
    #Kategorik veriler
    customer_id = np.random.randint(100,5000,size) #100,5000 arasında rastgele 1000 sayı üret
    products = np.random.choice(["Laptop","Phone","Monitor","Keyboard","Mouse","Hub","Tablet","Fon Makinesi", "Camasir Makinesi"], size) #listedeki ürünlerden 1000 adet seçiliyor
    city = np.random.choice(["İstanbul","Ankara","Mersin","Rize","Van","Aydın","Konya","Samsun","Denizli"],size)
    month = np.random.choice(["January","February","March","April","May","June","July"], size)
    amount = np.random.uniform(1000, 12000, size).round(2) #uniform ondalıklı üretir

    #Nan değerler ekle
    amount[2:12] = np.nan

    #Uç değerler ekle
    amount[30] = 80000
    amount[42] = 120500

    #Df oluşturalım
    df = pd.DataFrame({
        "CustomerID": customer_id,
        "Products": products,
        "City": city,
        "Month": month,
        "Amount": amount
    })

    return df