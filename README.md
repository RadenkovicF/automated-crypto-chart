**excel_crypto.py** &emsp;&emsp;&emsp; &emsp;Skript zum automatischen ausfüllen einer Excel tabelle mit aktuellen Kursen  
**get_id_by_symbol.py** &emsp;&emsp;kleines Skript zum holen der ID anahnd des Symbols (coinmarketcap)  
**price_alarm.py** &nbsp;&emsp;&emsp;&emsp;&emsp;kleines Skript für einen hardcoded preisalarm für TIME  
**prowl_push.py** &nbsp;&emsp;&emsp;&emsp;&emsp;enthält prowl push function, mit zugehöriger IOS app echtzeit Push Benachrichtigungen 
  
Mit raspberry pi und crontab leicht zu automatisieren.   
  
Coinmarketcap lässt 344 Anfragen am Tag zu.  
  
Bei mir läuft excel_crypto stündlich und der Preisalarm für time alle 5 Minuten,  
das entsprich 312 anfragen.
