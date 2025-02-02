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
        time.sleep(30)  # 30 saniyede bir kontrol et

reminder(15, 30, "Toplantı saati geldi!")
