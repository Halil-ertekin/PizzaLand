import csv
import datetime

with open('Menu.txt', 'w') as f:
    f.write('* Lütfen Bir Pizza Tabanı Seçiniz:\n')
    f.write('1: Klasik\n')
    f.write('2: Margarita\n')
    f.write('3: TürkPizza\n')
    f.write('4: Sade Pizza\n')
    f.write('* ve seçeceğiniz sos:\n')
    f.write('11: Zeytin\n')
    f.write('12: Mantarlar\n')
    f.write('13: Keçi Peyniri\n')
    f.write('14: Et\n')
    f.write('15: Soğan\n')
    f.write('16: Mısır\n')
    f.write('* Teşekkür ederiz!')


class Pizza:
    def __init__(self):
        self.description = "Bir pizza"
        
    def get_description(self):
        return self.description
    
    def get_cost(self):
        return 0.0


class Klasik(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza"
        
    def get_cost(self):
        return 20.0
    
class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita pizza"
        
    def get_cost(self):
        return 25.0
    
class TurkPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk pizzası"
        
    def get_cost(self):
        return 30.0
    
class SadePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Sade pizza"
        
    def get_cost(self):
        return 15.0

class Decorator(Pizza):
    def __init__(self, component):
        super().__init__()
        self.component = component
        
    def get_cost(self):
        return self.component.get_cost() + super().get_cost()
    
    def get_description(self):
        return self.component.get_description() + ", " + super().get_description()

class Zeytin(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Zeytin"
        
    def get_cost(self):
        return super().get_cost() + 2.0

class Mantarlar(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mantarlar"
        
    def get_cost(self):
        return super().get_cost() + 3.0
    
class KeciPeyniri(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Keçi Peyniri"
        
    def get_cost(self):
        return super().get_cost() + 7.0
    
class Et(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Et"
        
    def get_cost(self):
        return super().get_cost() + 10.0
    
class Sogan(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Soğan"
        
    def get_cost(self):
        return super().get_cost() + 2.0
    
class Misir(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "Mısır"
        
    def get_cost(self):
        return super().get_cost() + 4.0
    
def print_menu():
    with open('Menu.txt', 'r') as f:
        menu = f.read()
        print(menu)

def main():
    # Menüyü ekrana yazdırma
    print("Pizza Menüsü:")
    with open('Menu.txt', 'r') as f:
        print(f.read())

    pizzas = []
    while True:
        # Pizza seçimi yapma
        pizza_choice = input("Lütfen bir pizza seçin (1-4): ")
        if pizza_choice == "":
            break
        elif pizza_choice not in ["1", "2", "3", "4"]:
            print("Hatalı seçim, lütfen tekrar deneyin.")
            continue
        
    # Pizza oluşturma ve listeye ekleme
        if pizza_choice == "1":
            pizza = Klasik()
        elif pizza_choice == "2":
            pizza = Margarita()
        elif pizza_choice == "3":
            pizza = TurkPizza()
        elif pizza_choice == "4":
            pizza = SadePizza()
    
        while True:# Sos seçimi yapma
            print("Soslar:")
            with open('Menu.txt', 'r') as f:
                for i, line in enumerate(f):
                    if i > 4 and line.strip():
                        print(line.strip())
            sos_choice = input("Lütfen bir sos seçin (11-16): ")
            if sos_choice == "":
                break
            elif sos_choice not in ["11", "12", "13", "14", "15", "16"]:
                print("Hatalı seçim, lütfen tekrar deneyin.")
                continue

            #Sos ekleme
            if sos_choice == "11":
                pizza = Zeytin(pizza)
            elif sos_choice == "12":
                pizza = Mantarlar(pizza)
            elif sos_choice == "13":
                pizza = KeciPeyniri(pizza)
            elif sos_choice == "14":
                pizza = Et(pizza)
            elif sos_choice == "15":
                pizza = Sogan(pizza)
            elif sos_choice == "16":
                pizza = Misir(pizza)
        pizzas.append(pizza)

    # Sipariş özeti ve toplam fiyatı hesaplama
    total_cost = sum(pizza.get_cost() for pizza in pizzas)
    print("\nSipariş özeti:")
    for i, pizza in enumerate(pizzas, start=1):
        print(f"{i}. {pizza.get_description()} - {pizza.get_cost()} TL")
    print(f"\nToplam fiyat: {total_cost} TL")

    # Kullanıcı bilgileri alma ve veritabanına kaydetme
    name = input("İsim: ")
    id_number = input("TC Kimlik No: ")
    credit_card_number = input("Kredi Kartı No: ")
    credit_card_pin = input("Kredi Kartı Şifresi: ")

    with open('Orders_Database.csv', 'a') as f:
        writer = csv.writer(f)
        timestamp = datetime.datetime.now()
        for pizza in pizzas:
            writer.writerow([pizza.get_description().split(",")[0], name, id_number, credit_card_number, pizza.get_description(), timestamp, credit_card_pin])


if __name__ == "__main__":
    main()