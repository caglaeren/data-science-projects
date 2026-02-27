# Veri temizleme 
import numpy as np
import pandas as pd

"""Veri temizleme fonksiyonu"""
def preprocessing_data(df, vergi = 0.25):  #KDV oranı default %25
    try:
        #Eksik verileri tespit et
        missing_data = df.isnull().sum() #eksik verileri buldu ve hepsini topladı
        print(f"Eksik veri sayısı: {missing_data}")

        #Eksik verileri Sil/Doldur
        #Amount'u sayıya çevirelim eğer bozuk sayı falan gelirse diye
        #eğer içinde metin varsa Nan yapar errors=coerce ile 
        if df["Amount"].dtype == "object": #eğer satış mik metinse
            df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")

        #Amount eksikse mean / median ile doldur
        df["Amount"] = df["Amount"].fillna(df["Amount"].median()) #medyanla doldurduk

        #City'de eksik varsa önce doldurmayı deneyelim olmazsa silelim
        if df["City"].isnull().any():
            try: #mode varsa dolduralım
                df["City"] = df["City"].fillna(df["City"].mode()[0]) #en sık görülen değerle döndürür
            except:
                df = df.dropna(subset=["City"]) #dolduramazsa siler

        #Product için de eksikse dolduralım dolduramazsak silelim
        if df["Products"].isnull().any():
            try:
                df["Products"] = df["Products"].fillna(df["Products"].mode()[0])
            except:
                df = df.dropna(subset=["Products"])
                
        #Month'daki veriler eksikse 
        if df["Month"].isnull().any():
            try:
                df["Month"] = df["Month"].fillna(df["Month"].mode()[0])
            except:
                df = df.dropna(subset=["Month"])

        
        #String kolonları normalize et
        #şehir isimlerini standart hale getirir
        #str.strip() -> başındaki ve sonundaki boşlukları siler
        #str.title() -> her kelimenin ilk harfini büyütür
        df["City"] = df["City"].astype(str).str.strip().str.title() #(Büyük harf ve boşluk temizliği)
        df["Products"] = df["Products"].astype(str).str.strip().str.upper() #bütün harfleri büyütür
        df["Month"] = df["Month"].astype(str).str.strip().str[:3].str.title() #0.'dan 3.indekse kadar al

        #Yeni sütunlar üret (KDV'li satış vb)
        df["KDV"] = df["Amount"] * (1 + vergi)

        #satış büyüklüğüne göre kategori eklesek
        df["Sale Category"] = "Basic"
        df.loc[df["Amount"] >= 2500, "Sale Category"] = "Standard"
        df.loc[df["Amount"] >= 4000, "Sale Category" ] = "High"
        df.loc[df["Amount"] >= 9000, "Sale Category" ] = "Platinum"

        return df
        
    except KeyError as e:
        #Beklenen kolon yoksa mesela (City gibi)
        print(f"Kolon bulunamadı. {e}")
        print("Beklenen kolonlar: City, Products, Amount, Month")
        return df
    except Exception as ex:
        #her türlü beklenmeyen hata için
        print(f"Preprocessing (on isleme) hatası: {ex}")
        return df
        
                                        
        