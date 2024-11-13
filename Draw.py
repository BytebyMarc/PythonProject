class Draw:
    @staticmethod
    def start():
        print("Das Programm wurde gestartet")
        print("Menü")
        print("1. Gerade aus Fahren")
        print("2. Rückwährtsfahren")
        print("3. Links")
        print("4. Rechts")
        print("5. Stop")
        print("6. Sonderfunktionen")
        print("10. Beenden")

    @staticmethod
    def straightAhead():
        print("Sie fahren Vorwährts")

    @staticmethod
    def returns():
        print("Sie fahren Rückwährts")

    @staticmethod
    def left():
        print("Sie fahren nach links")

    @staticmethod
    def right():
        print("Sie fahren nach rechts")

    @staticmethod
    def stop():
        print("STOP")

