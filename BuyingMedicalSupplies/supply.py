class Supply:
    def __init__(self, supply_name, quantity_in_stock, ideal_stock, price):
        self.supply_name = supply_name
        self.quantity_in_stock = quantity_in_stock
        self.ideal_stock = ideal_stock
        self.price = price
        self.percentage_in_stock = (quantity_in_stock*100)/ideal_stock
        self.percentage_in_need = (100 - self.percentage_in_stock)
        self.cost_benefit = (self.percentage_in_need / self.price)

    def print_data(self):
        print("------------------------------------------")
        print(f"Supply: {self.supply_name}")
        print(f"Current Stock: {self.quantity_in_stock}")
        print(f"Max Stock: {self.ideal_stock}")
        print(f"Price: {self.price}")
        print(f"percentage in Stock: {self.percentage_in_stock}")
        print(f"Percentage missing: {self.percentage_in_need}")
        print(f"Cost Benefit: {self.cost_benefit}")

    def return_data(self):
        s = ""
        s += "-----------------------------------------------------\n"
        s += f"Supply: {self.supply_name}\n"
        s += f"Current Stock: {self.quantity_in_stock}\n"
        s += f"Max Stock: {self.ideal_stock}\n"
        s += f"Price: {self.price}\n"
        s += f"percentage in Stock: {self.percentage_in_stock}\n"
        s += f"Percentage missing: {self.percentage_in_need}\n"
        s += f"Cost Benefit: {self.cost_benefit}"
        return s
