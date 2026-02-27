# Analitik motor
#Numpy ile normalize edilmiş matrisler ve performans skorları
#Pandas ile şehir bazlı satış, ürün bazlı satış, ay bazlı trend
#Groupby + agg kullan (Loop yok)
import numpy as np
import pandas as od

def sales_matrix(df):
    # City x Product matrisi (toplam satış)
    #pivot tablo -> veriyi satır-sütun matrisi haline getirerek analiz ve karşılaştırmayı kolaylaştırır.
    #Satış verisini Şehir x ürün matrisi yapar
    #index -> satırlar şehir, columns-> sütunlar ürün, tabloya konan değer satış tutarı
    # aggfunc="sum" -> aynı şehir + ürün birden fazla varsa toplamını alır
    #fill_valeus =0 -> eğer o şehirde ürün satılmamışsa boş yerine 0 koyar
    return df.pivot_table(index="City", columns="Products", values="Amount", aggfunc = "sum", fill_value=0)

def normalize_matrix(matrix_df):
    #min-max normalize (0-1 arası)
    #laptop sütunu kendi içinde normalize, mouse sütunu kendi içinde normalize olur
    min_val = matrix_df.min(axis=0)
    max_val = matrix_df.max(axis=0)
    return (matrix_df - min_val) / (max_val - min_val)

def performance_score(normalize_df):
    #Noramlize edilmiş satırlara göre şehirleri sıralayalım
    #şehir performans skoru = satır ortalaması alarak 
    #şehirler satırlardır
    #ascending_False -> büyükten küçüğe sıralar yani en güçlü şehir en üstte
    return normalize_df.mean(axis=1).sort_values(ascending=False) #axis=1 demek her şehrin ortalama perf

def city_sale(df):
    #veriyi şehirlere göre grupladık ve satış verisini bulduk , top satış, ort satış, kaç satış yapıldı hesapladık ve toplam satışa göre sıraladık. en çok satan en üstte olacak
    return df.groupby("City")["Amount"].agg(["sum", "mean","count"]).sort_values("sum", ascending=False)

def product_sale(df):
    #Veriyi ürünlere göre grupladık ve en çok hangi ürün satmış onu bulduk ve toplam satışa göre sıraladık
    return df.groupby("Products")["Amount"].agg(["sum", "mean","count"]).sort_values("sum", ascending=False)

def monthly_trend(df):
    #Veriyi ay bazlı analiz ettik ve hangi ay satışlar artmış hangi ay düşmüş onu görürürz
    return df.groupby("Month")["Amount"].agg(["sum", "mean","count"])
    
    
    
