#Karar destek katmanı
# En iyi / en kötü şehir
# En karlı ürün
# Risklli bölgeler (düşük ort)
# Yöneticiye okunabilir özet üret 
import pandas as pd
import numpy as np

def decision_report(city_report, product_report):
    #index -> şehir adı, sum =toplam satış
    #city_report["sum"] -> toplam satış sütunlarını alır ve max ile en büyük değeri verir
    #tuple kullanarak -> en iyi şehir + satış miktarı yapıldı
    best_city = (city_report["sum"].idxmax(), city_report["sum"].max())
    worst_city = (city_report["sum"].idxmin(), city_report["sum"].min())

    best_product = (product_report["sum"].idxmax(), product_report["sum"].max())

    #Riskli bölgeler (düşük ortalama)
    risk = city_report[city_report["mean"] < 2000]
    risk_varmi = len(risk) > 0 #bool

    #dictionary
    report = {
        "Best City" : best_city,
        "Worst City" : worst_city,
        "Best Product" : best_product,
        "Has Risk" : risk_varmi
    }

    #Okunabilir özet
    print(f"En iyi şehir: {report['Best City']}")
    print(f"En kötü şehir: {report['Worst City']}")
    print(f"En karlı ürün: {report['Best Product']}")
    if report['Has Risk']:
        print(f"Riskli şehirler var:\n {risk}")
    else:
        print("Riskli şehir yok.")

    return report
        