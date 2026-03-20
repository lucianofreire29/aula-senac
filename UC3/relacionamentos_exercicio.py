class User:
    def __init__(self,id:int , name: str, email: str, password: str,):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.orders = list()

    def generate_report(self):
        report =f"ID {self.id} | name: {self.name} | email: {self.email} | password: {self.password} "

        for order in self.orders:
            report += order.generate_report() + "\n"


        return report


class Order:
    def __init__(self,id: int, date: str ):
        self.id = id
        self.date = date
        self.products = list()
        self.total_amount = 0

    def calc_total_amount(self) -> float:
        total = 0
        for product in self.products:
            total += product.value
            self.total_amount = total

        return total


    def generate_report(self):
        report = f"Pedido {self.id} - Data: {self.date}\n"

        for product in self.products:
            report += product.info() + "\n"

        report += f"Total: {self.total_amount}"
        return report


class Product:
    def __init__(self,id: int, name: str, value: float, description: str):
        self.id = id
        self.name = name
        self.value = value
        self.description = description

    def info(self):
        return f" {self.id} | {self.name} | {self.value} | {self.description}"









# TESTE

p1 = Product(1, "Mouse", 80.0, "Mouse gamer")
p2 = Product(2, "Teclado", 150.0, "Teclado mecânico")

order = Order(1, "29/01/2026")
order.products.append(p1)
order.products.append(p2)
order.calc_total_amount()

user = User(1, "Luciano", "luciano.freire@email.com", "1234")
user.orders.append(order)

print(user.generate_report())