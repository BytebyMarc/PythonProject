class Draw:
    @staticmethod
    def start():
        print("Das Programm wurde gestartet")
        print("Menü")
        print("1.  Freies Fahren")
        print("2.  Automatisiert Liene folgen")
        print("3.  Sensor Test") # abfrage alle 1-2 sekunden automatisiert
        print("4.  Motoren Test")
        print("5.  Setup") # Wifi # max geschwindigkeit
        print("6.  Reboot")
        print("10. Shutdown")

    @staticmethod
    def freeDrive():
        print("Sie sind im Menüpunkt Freies Fahren")

    @staticmethod
    def sensorAutoDrive ():
        print("Fahre Automatisiert")

    @staticmethod
    def sensorTest():
        print("Der Sensor Test startet in wenigen Sekunden")

    @staticmethod
    def motorTest():
        print("!!!Achtung!!! Der Motoren Test startet in 3 Sekunden")

    @staticmethod
    def setup():
        print("Sie sind im Setup Menü:")

    @staticmethod
    def reboot():
        print("Reboot")
    @staticmethod
    def stop():
        print("Shutdown")

