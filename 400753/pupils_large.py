import time

# Değişkenleri başlat
sum_marks = 0   # Tüm notların toplamı
amount = 0      # Toplam öğrenci sayısı
best_pupils = []  # Notu 5 olan öğrenciler

start_time = time.time()

# Dosyayı satır satır okuyarak işleme
with open("pupil_large.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.split()
        surname = data[0]  # Soyadı al
        mark = int(data[2])  # Notu al

        # Toplam not ve öğrenci sayısını güncelle
        sum_marks += mark
        amount += 1

        # Eğer not 5 ise, başarılı öğrenciler listesine ekle
        if mark == 5:
            best_pupils.append(surname)

# Ortalama hesaplama
average = sum_marks / amount if amount > 0 else 0

# Sonuçları yazdır
print("Başarılı öğrenciler:", ", ".join(best_pupils))
print("Sınıfın ortalama notu:", round(average, 2))
print("Gerçekleştirme süresi:", round(time.time() - start_time, 4), "saniye")
