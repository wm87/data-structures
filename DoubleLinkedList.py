class DoubleNode:
    def __init__(self, daten):
        self.daten = daten
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.kopf = None

    def ist_leer(self):
        return self.kopf is None

    def laenge(self):
        count = 0
        aktueller = self.kopf
        while aktueller:
            count += 1
            aktueller = aktueller.next
        return count

    def anzeigen_vorwaerts(self):
        print("Vorwärts:")
        aktueller = self.kopf
        while aktueller:
            print(aktueller.daten, end=" <-> ")
            aktueller = aktueller.next
        print("None")

    def anzeigen_rueckwaerts(self):
        print("Rückwärts:")
        aktueller = self.kopf
        if not aktueller:
            print("None")
            return
        while aktueller.next:
            aktueller = aktueller.next
        while aktueller:
            print(aktueller.daten, end=" <-> ")
            aktueller = aktueller.prev
        print("None")

    def am_anfang_einfuegen(self, daten):
        neuer_knoten = DoubleNode(daten)
        if self.kopf:
            self.kopf.prev = neuer_knoten
            neuer_knoten.next = self.kopf
        self.kopf = neuer_knoten

    def am_ende_einfuegen(self, daten):
        neuer_knoten = DoubleNode(daten)
        if not self.kopf:
            self.kopf = neuer_knoten
            return
        aktueller = self.kopf
        while aktueller.next:
            aktueller = aktueller.next
        aktueller.next = neuer_knoten
        neuer_knoten.prev = aktueller

    def einfuegen_an_position(self, daten, position):
        if position <= 0:
            self.am_anfang_einfuegen(daten)
            return
        if position >= self.laenge():
            self.am_ende_einfuegen(daten)
            return
        neuer_knoten = DoubleNode(daten)
        aktueller = self.kopf
        for _ in range(position):
            aktueller = aktueller.next
        vorheriger = aktueller.prev
        vorheriger.next = neuer_knoten
        neuer_knoten.prev = vorheriger
        neuer_knoten.next = aktueller
        aktueller.prev = neuer_knoten

    def loesche_knoten(self, daten):
        aktueller = self.kopf
        while aktueller:
            if aktueller.daten == daten:
                if aktueller.prev:
                    aktueller.prev.next = aktueller.next
                else:
                    self.kopf = aktueller.next  # Kopf löschen
                if aktueller.next:
                    aktueller.next.prev = aktueller.prev
                return True
            aktueller = aktueller.next
        return False  # nicht gefunden

    def loesche_an_index(self, index):
        if index < 0 or index >= self.laenge():
            print("Ungültiger Index")
            return
        aktueller = self.kopf
        for _ in range(index):
            aktueller = aktueller.next
        if aktueller.prev:
            aktueller.prev.next = aktueller.next
        else:
            self.kopf = aktueller.next
        if aktueller.next:
            aktueller.next.prev = aktueller.prev

    def suche(self, daten):
        index = 0
        aktueller = self.kopf
        while aktueller:
            if aktueller.daten == daten:
                return index
            aktueller = aktueller.next
            index += 1
        return -1




if __name__ == "__main__":
    liste = DoublyLinkedList()

    liste.am_anfang_einfuegen("C")
    liste.am_anfang_einfuegen("B")
    liste.am_anfang_einfuegen("A")  # A <-> B <-> C
    liste.am_ende_einfuegen("E")  # A <-> B <-> C <-> E
    liste.einfuegen_an_position("D", 3)  # A <-> B <-> C <-> D <-> E

    liste.anzeigen_vorwaerts()
    liste.anzeigen_rueckwaerts()

    print("\nIndex von 'C':", liste.suche("C"))
    print("Lösche 'B':", liste.loesche_knoten("B"))
    liste.anzeigen_vorwaerts()

    print("\nLösche an Index 2:")
    liste.loesche_an_index(2)
    liste.anzeigen_vorwaerts()

    print("\nLänge der Liste:", liste.laenge())
    print("Ist die Liste leer?", liste.ist_leer())

