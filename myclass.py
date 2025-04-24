class Phone:
    def __init__(self, brand, model, color, price):
        self.brand = brand
        self.model = model
        self.color = color
        self.price = price
    
class Business_phone(Phone):
    def __init__(self, brand, model, color, price):
        super().__init__(brand, model, color, price)
        self.model = model
        
    def Picture_phone(self, picture):
        print(f"Taking a picture with {self.brand} {self.model} in {self.color} color!")    
    
    def Business_call(self, business_name, phone_number):
        print(f"Calling {business_name} at {phone_number} using {self.brand} {self.model}!")

    
my_phone1 = Phone("Apple", "iPhone 14", "Black", "$999")
my_phone2 = Phone("Samsung", "Galaxy S23", "White", "$799")
my_phone3 = Phone("Google", "Pixel 7", "Green", "$599")
print(my_phone1.brand, my_phone1.model, my_phone1.color, my_phone1.price)

picture_phone1 = Picture_phone("Apple", "iPhone 14", "Black", "$999")
picture_phone1.Picture_phone("selfie")

Business_phone1 = Business_phone("Samsung", "Galaxy S23", "White", "$799")
Business_phone1.Business_call("Senator", "0816666778")