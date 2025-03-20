import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)  
maaslar = np.random.randint(3000, 15001, size=500)

print("İlk 10 kişinin maaşları:", maaslar[:10])
ortalama_maas = np.mean(maaslar)
max_maas = np.max(maaslar)
min_maas = np.min(maaslar)

print(f"Ortalama Maaş: {ortalama_maas:.2f} TL")
print(f"Maksimum Maaş: {max_maas} TL")
print(f"Minimum Maaş: {min_maas} TL")

plt.figure(figsize=(10, 6))
plt.hist(maaslar, bins=20)
plt.title('Çalışan Maaş Dağılımı')
plt.xlabel('Maaş (TL)')
plt.ylabel('Çalışan Sayısı')
plt.grid(True)
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# 📌 Rastgele veri üretimi için seed belirleyelim (Aynı sonuçları almak için)
np.random.seed(42)

# 📊 500 çalışanın maaşlarını rastgele belirle (3000 TL - 15000 TL arasında)
maaslar = np.random.randint(3000, 15000, 500)

# 🏢 Çalışanları 3 farklı departmana rastgele ata
departmanlar = np.random.choice([1, 2, 3], size=500)

# 📌 Departman bazında maaşları hesaplayalım
muhendislik_maas = maaslar[departmanlar == 1]
muhasebe_maas = maaslar[departmanlar == 2]
pazarlama_maas = maaslar[departmanlar == 3]

# 📊 Her departmanın ortalama maaşını hesapla
ortalama_muhendislik = np.mean(muhendislik_maas)
ortalama_muhasebe = np.mean(muhasebe_maas)
ortalama_pazarlama = np.mean(pazarlama_maas)

# 📌 Sonuçları ekrana yazdır
print(f"📊 Departman Bazlı Maaş Analizi:")
print(f"🏗️ Mühendislik Ortalama Maaş: {ortalama_muhendislik:.2f} TL")
print(f"📊 Muhasebe Ortalama Maaş: {ortalama_muhasebe:.2f} TL")
print(f"📢 Pazarlama Ortalama Maaş: {ortalama_pazarlama:.2f} TL")

# 📈 Departman bazında maaş dağılımı için bar grafiği çizelim
departman_isimleri = ["Mühendislik", "Muhasebe", "Pazarlama"]
ortalama_maaslar = [ortalama_muhendislik, ortalama_muhasebe, ortalama_pazarlama]

plt.figure(figsize=(8, 5))
plt.bar(departman_isimleri, ortalama_maaslar, color=["blue", "green", "red"])
plt.xlabel("Departmanlar")
plt.ylabel("Ortalama Maaş (TL)")
plt.title("Departman Bazlı Ortalama Maaşlar")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()

# 📌 GÖREV 3: Bir Yıl Boyunca Günlük Sıcaklık Değerleri Simülasyonu

# 🌡️ 365 günlük sıcaklık değerlerini -10°C ile 40°C arasında rastgele üret
sicakliklar = np.random.uniform(-10, 40, 365)

# 📊 Ortalama, en sıcak ve en soğuk günü hesapla
ortalama_sicaklik = np.mean(sicakliklar)
en_sicak_gun = np.max(sicakliklar)
en_soguk_gun = np.min(sicakliklar)

# 📌 Sonuçları yazdır
print(f"📉 Hava Durumu Analizi:")
print(f"🌡️ Ortalama Sıcaklık: {ortalama_sicaklik:.2f}°C")
print(f"🔥 En Sıcak Gün: {en_sicak_gun:.2f}°C")
print(f"❄️ En Soğuk Gün: {en_soguk_gun:.2f}°C")

# 📈 Günlük sıcaklık değişimlerini görselleştirme
gunler = np.arange(1, 366)  # 1’den 365’e kadar günler

plt.figure(figsize=(10, 5))
plt.plot(gunler, sicakliklar, color="orange", linestyle="-", marker=".", markersize=3)
plt.xlabel("Günler")
plt.ylabel("Sıcaklık (°C)")
plt.title("Yıllık Günlük Sıcaklık Değişimi")
plt.axhline(y=ortalama_sicaklik, color="red", linestyle="--", label=f"Ortalama: {ortalama_sicaklik:.2f}°C")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()

# 📌 GÖREV 4: Ürün Satış Analizi

# 🛒 5 farklı ürün ve 30 günlük satış verilerini simüle et
urunler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
gun_sayisi = 30
np.random.seed(42)  # Aynı sonuçları almak için

# 📊 Her ürün için 30 günlük rastgele satış miktarları (10-100 arası)
satis_verileri = np.random.randint(10, 100, (5, gun_sayisi))

# 📌 Toplam ve ortalama satış miktarlarını hesapla
toplam_satislar = np.sum(satis_verileri, axis=1)
ortalama_satislar = np.mean(satis_verileri, axis=1)

# 📌 Sonuçları yazdır
print(f"📈 Ürün Satış Analizi:")
for i in range(len(urunler)):
    print(f"{urunler[i]} - Toplam Satış: {toplam_satislar[i]}, Ortalama Satış: {ortalama_satislar[i]:.2f}")

# 📊 Ürün bazında çubuk grafiği oluştur
plt.figure(figsize=(8, 5))
plt.bar(urunler, toplam_satislar, color=["blue", "green", "red", "purple", "orange"])
plt.xlabel("Ürünler")
plt.ylabel("Toplam Satış Miktarı")
plt.title("Ürün Bazında Toplam Satışlar")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
