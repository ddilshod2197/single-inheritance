class Avto:
    def __init__(self, rahbar, korobka):
        self.rahbar = rahbar
        self.korobka = korobka

class AvtoMashina(Avto):
    def __init__(self, rahbar, korobka, dvigatel):
        super().__init__(rahbar, korobka)
        self.dvigatel = dvigatel

avto = AvtoMashina("Rahbar", "Korobka", "Dvigatel")
print(avto.rahbar)  # Rahbar
print(avto.korobka)  # Korobka
print(avto.dvigatel)  # Dvigatel
```

```python
class Avto:
    def __init__(self, rahbar, korobka):
        self.rahbar = rahbar
        self.korobka = korobka

class AvtoMashina(Avto):
    def __init__(self, rahbar, korobka, dvigatel):
        super().__init__(rahbar, korobka)
        self.dvigatel = dvigatel

class AvtoTraktor(Avto):
    def __init__(self, rahbar, korobka, dvigatel, kran):
        super().__init__(rahbar, korobka)
        self.dvigatel = dvigatel
        self.kran = kran

avto_mashina = AvtoMashina("Rahbar", "Korobka", "Dvigatel")
avto_traktor = AvtoTraktor("Rahbar", "Korobka", "Dvigatel", "Kran")
print(avto_mashina.rahbar)  # Rahbar
print(avto_mashina.korobka)  # Korobka
print(avto_mashina.dvigatel)  # Dvigatel
print(avto_traktor.rahbar)  # Rahbar
print(avto_traktor.korobka)  # Korobka
print(avto_traktor.dvigatel)  # Dvigatel
print(avto_traktor.kran)  # Kran
