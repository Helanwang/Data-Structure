class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int = 1):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    # without this method, it will print the Product ID: <__main__.Product object at 0x104260c20>
    # Now is printing: 542: Brandy 34.99 2
    def __str__(self):
        return f"{self.product_id}: {self.name} {self.price} {self.quantity}"

    def display_product(self):
        print(self.product_id, self.name, self.price, self.quantity)


crop_top = Product("542", "Brandy", 34.99, 2)
crop_top.display_product()
print(crop_top)  # Output: <__main__.Product object at 0x104260c20>
print(str(crop_top))


class Employee:
    def __init__(self, employee_id: str, name: str, position: str, salary: float, years_of_experience: int):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.years_of_experience = years_of_experience

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}, {self.years_of_experience}"

    def promotion(self, company):
        print(f"This new employee is promoted in {company} company!!")


helen_wang = Employee("1121", "Helen Wang", "Software Engineer", 150000.32,
                      2)

print(helen_wang)
helen_wang.promotion("Google")


class BrandyMelville:

    owner = "Lindy Karen"
    location = "Palo Alto"

    def __init__(self, item_id: str, name: str, price: float, stock: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return (f"The item ID: {self.item_id}, the name is : {self.name}, the price is: {self.price}, the stock is: "
                f"{self.stock} the location is {self.location}")

    def scanning(self):
        print(f"this {self.name}, with ID: {self.item_id} is scanning right now ! Be patient:) Lovely")


tank_top = BrandyMelville("4569", "Navy Blue Tank Top", 29.98, 20)
crop_top = BrandyMelville("5821", "Pink Crop Top", 15.69, 10)
skirts = BrandyMelville("8545", "Red Skirts", 11.98, 5)

print(tank_top)
tank_top.scanning()
print(tank_top.owner)


print(crop_top)
skirts.scanning()

print(skirts)
skirts.scanning()


class Student:

    school = "Foothill College"

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_emails(self):
        print(f"{self.first_name}.{self.last_name}@gmail.com")


Helen_Wang = Student("Helen", "Wang")
Helen_Wang.get_emails()
