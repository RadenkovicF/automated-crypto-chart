**excel_crypto.py** &emsp;&emsp;&emsp; &emsp;Skript zum automatischen ausfüllen einer Excel tabelle mit aktuellen Kursen  
**get_id_by_symbol.py** &emsp;&emsp;kleines Skript zum holen der ID anahnd des Symbols (coinmarketcap)  
**price_alarm.py** &nbsp;&emsp;&emsp;&emsp;&emsp;kleines Skript für einen hardcoded preisalarm für TIME  
**prowl_push.py** &nbsp;&emsp;&emsp;&emsp;&emsp;enthält prowl push function, mit zugehöriger IOS app echtzeit Push Benachrichtigungen 
  
Mit raspberry pi und crontab leicht zu automatisieren.   Mit rclone und googledrive online auf das Dokument zugreifen  Mit "linger" dafür sorgen, dass user nicht abgemeldet wird.
  Datei in crontab eintrag darf nicht im mounted drive verzeichnis sein.       
    Annahme: excel_crypto.py und die Excel Tabelle wurden ins main verzeichnis kopiert:
crontab -e am ende des Files eintrag:  
0 * * * * /usr/bin/python /home/pi/excel_crypto.py  
2 * * * * cp /home/pi/crypto_geld.xlsx /home/pi/PFADMNTDRIVE/crypto_geld.xlsx  
*/5 * * * * /usr/bin/python /home/pi/ /home/pi/price_alarm.py    




  
Coinmarketcap lässt 344 Anfragen am Tag zu.  
  
Bei mir läuft excel_crypto stündlich und der Preisalarm für time alle 5 Minuten,  
das entsprich 312 anfragen.
