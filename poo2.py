class Persona:
    name = str
    age = int
    gender = str
    balance = int
    acount_number = int
    deposit = int
    withdraw = int


    def __init__(self, name:str, age:int,gender:str):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self)->str:
        return (f'Mi name is {self.name} and I am {self.age} years old, im a {self.gender}')  

   
class CuentaBancaria:
   

    def __init__(self, owner: Persona, balance: int, account_number: int):
        self.owner = owner
        self.balance = balance
        self.account_number = account_number
    
    def depositar(self):
        deposit = float(input("Type the amount you want to deposit: "))
        if deposit > 0:
            self.balance += deposit
            print(f"Successful deposit. Your current balance is ${self.balance}")
        else:
            print("The deposit amount must be greater than 0.")
    
    def retirar(self):
        withdraw = float(input("Type the amount you want to withdraw: "))
        if 0 < withdraw <= self.balance:
            self.balance -= withdraw
            print(f"Successful withdrawal. Your new balance is: ${self.balance}")   
        else:
            print(f"You cannot withdraw that amount. Your balance is ${self.balance}")
    
    def consultar(self):
        print(f"Your current balance is ${self.balance}")
    
    def __str__(self)->str:
        return f"Bank account of {self.owner.name}, Account number: {self.account_number}, Balance: ${self.balance}"
    
class Rectangulo:
    base = int
    altura = int

    def __init__(self, base: int, altura: int):
        self.base = base
        self.altura = altura
    
    def area(self):
        return f"the area of  the rectangle is {self.base * self.altura} " 
    
    def perimetro(self):
        return f"the perimeter of  the rectangle is {2 * (self.base + self.altura)}"
    
    def __str__(self):
        return f"Rectangle with base {self.base} and height {self.altura}"    
    
class Libro:
    title = str
    author = str
    year = int
    genre = str


    def __init__(self, title:str, author:str, year:int, genre:str):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __str__(self)->str:
        return (f'The book {self.title} was written by {self.author} in {self.year}, it is a {self.genre} book')  
    
class Cancion:
    title = str
    artist = str
    album = str
    duration = int

    def __init__(self, title:str, artist:str, album:str,  duration:int):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration

    def __str__(self)->str:
        return (f'The song {self.title} is from the album {self.album} by {self.artist}, and it lasts {self.duration} seconds')   

class Producto:
    product_name = str
    price = float
    stock = int 

    def __init__(self, product_name: str, price: float, stock: int):
        self.product_name = product_name
        self.price = price
        self.stock = stock

    def calcular_total(self, amount: int):
        if amount > self.stock:
            return "No hay suficiente stock disponible."
        return amount * self.price
    
    def __str__(self)->str:
        return f"Producto: {self.product_name}, Precio: ${self.price}, Stock: {self.stock} unidades"
    
class Estudiante:
    nombre= str
    edad = int
    curso = str

    def __init__(self, nombre: str, edad: int, curso: str):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []
    
    def agregar_calificacion(self, calificacion: float):
        self.calificaciones.append(calificacion)
    
    def calcular_promedio(self):
        if not self.calificaciones:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)
    
    def esta_aprobado(self):
        return self.calcular_promedio() >= 3.0
    
    def __str__(self):
        return f"Estudiante: {self.nombre}, Edad: {self.edad}, Curso: {self.curso}, Promedio: {self.calcular_promedio()}"

persona1 = Persona("Juan", 25, "Man")
print(persona1)

account_persona = CuentaBancaria(persona1, balance=200, account_number=12356)
print(account_persona)
account_persona.consultar()
account_persona.depositar()
account_persona.retirar()
account_persona.consultar()

rectangulo1 = Rectangulo(5, 10)
print(rectangulo1)
print(rectangulo1.area())
print(rectangulo1.perimetro())

book1 = Libro("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1977, "Fantasy")
print(book1)

sonng1 = Cancion("Bohemian Rhapsody", "Queen", "A Night at the Opera", 354)
print(sonng1)

producto1 = Producto("Laptop", 1500.00, 10)
print(producto1)
print(f"Total por 3 unidades: ${producto1.calcular_total(5)}")

estudiante1 = Estudiante("Carlos", 20, "Matemáticas")
estudiante1.agregar_calificacion(3.5)
estudiante1.agregar_calificacion(4.0)
estudiante1.agregar_calificacion(5.0)
print(estudiante1)
print(f"¿El estudiante aprobó?: {'Sí' if estudiante1.esta_aprobado() else 'No'}")