# 📌 Python Hatırlatma Otomasyonu

Bu proje, belirli bir saatte ekrana bildirim göstererek kullanıcıya hatırlatma yapar. Kullanıcı belirttiği saate geldiğinde, bilgisayarında bir bildirim alır.

## 🚀 Özellikler
- Belirli bir saat ve dakikada hatırlatma yapar.
- Windows, macOS ve Linux ile uyumludur.
- **`plyer`** kütüphanesi ile bildirim gönderir.

## 📦 Gerekli Kütüphaneler
Bu projeyi çalıştırmadan önce aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

```bash
pip install plyer
```

## 📝 Kullanım
Python dosyanızı çalıştırmadan önce, hatırlatma saatini ve mesajınızı ayarlayın.

```python
import time
from datetime import datetime
from plyer import notification

def reminder(set_hour, set_minute, message):
    while True:
        now = datetime.now()
        if now.hour == set_hour and now.minute == set_minute:
            notification.notify(
                title="Hatırlatma",
                message=message,
                timeout=5
            )
            break
        time.sleep(30)  # 30 saniyede bir kontrol eder

reminder(15, 30, "Toplantı saati geldi!")
```

### 🛠️ Parametreler
- **set_hour**: Hatırlatma saati (0-23 arasında)
- **set_minute**: Hatırlatma dakikası (0-59 arasında)
- **message**: Bildirimde gösterilecek mesaj

## 🎯 Örnek Kullanım
Eğer her gün saat **09:00'da** "Günaydın! Çalışmaya başlama vakti." mesajı almak istiyorsanız:

```python
reminder(9, 0, "Günaydın! Çalışmaya başlama vakti.")
```

## 📌 Notlar
- Program arka planda çalışmaya devam eder. Durdurmak için terminali kapatabilirsiniz.
- **Windows için** bildirimlerin çalışması için bildirimlerin açık olduğundan emin olun.
- **MacOS'ta** terminale şu komutu girerek bildirimleri etkinleştirebilirsiniz:
  ```bash
  defaults write com.apple.notificationcenterui bannerTime 5
  ```

## 📜 Lisans
Bu proje MIT lisansı ile lisanslanmıştır. Özgürce kullanabilirsiniz. 🎉
