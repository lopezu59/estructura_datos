class Empleado:
    nombre= str
    salario = float
    departamento = str
    
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        return f"{self.nombre} está trabajando en {self.departamento}."

class Gerente(Empleado):
    equipo = list

    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo
    
    def supervisar_equipo(self):
        return f"{self.nombre} está supervisando a su equipo."

class Desarrollador(Empleado):
    lenguaje = str

    def __init__(self, nombre: str, salario: float, departamento: str, lenguaje: str):
        super().__init__(nombre, salario, departamento)
        self.lenguaje = lenguaje
    
    def escribir_codigo(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje}."

class FiguraGeometrica:
    def calcular_area(self):
        pass

class Triangulo(FiguraGeometrica):
    base = float
    altura = float

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    lado = float    

    def __init__(self, lado: float):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

class Electrodomestico:
    marca = str
    modelo = str
    consumo = str

    def __init__(self, marca: str, modelo: str, consumo: str):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo
    
    def encender(self):
        return f"{self.marca} {self.modelo} está encendido."

class Lavadora(Electrodomestico):
    capacidad = float

    def __init__(self, marca: str, modelo: str, consumo: str, capacidad: float):
        super().__init__(marca, modelo, consumo)
        self.capacidad = capacidad
    
    def iniciar_ciclo(self):
        return f"Lavadora {self.marca} iniciando ciclo de lavado."

class Refrigerador(Electrodomestico):
    tiene_congelador = bool

    def __init__(self, marca: str, modelo: str, consumo: str, tiene_congelador: bool):
        super().__init__(marca, modelo, consumo)
        self.tiene_congelador = tiene_congelador
    
    def regular_temperatura(self):
        return f"Regulando temperatura del refrigerador {self.marca}."

class Usuario:
    nombre_usuario = str
    contraseña = str
    
    def __init__(self, nombre_usuario: str, contrasena: str):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
    
    def iniciar_sesion(self, usuario: str, contrasena: str):
        if self.nombre_usuario == usuario and self.contrasena == contrasena:
            print(f"Inicio de sesión exitoso para {self.nombre_usuario}.")
            return True
        else:
            print("Las credenciales son incorrectas.")
            return False

class Administrador(Usuario):
    def gestionar_usuarios(self):
        if self.nombre_usuario == "admin" and self.contrasena == "1234":
            print("Gestionando usuarios del sistema.")
        else:
            print("No tienes permisos para gestionar usuarios.")

class Cliente(Usuario):
    def realizar_compra(self):
        if self.nombre_usuario =="cliente1"  and self.contrasena == "abcd":
            print("Compra realizada con éxito.")
        else:
            print("No puedes realizar compras sin iniciar sesión correctamente.")
    
    
empleado1 = Empleado("Carlos", 3000, "Ventas")
print(empleado1.trabajar())

gerente1 = Gerente("Laura", 5000, "Recursos Humanos", ["Carlos", "Ana"])
print(gerente1.trabajar())
print(gerente1.supervisar_equipo())

dev1 = Desarrollador("Pedro", 4000, "TI", "Python")
print(dev1.trabajar())
print(dev1.escribir_codigo())

triangulo1 = Triangulo(10, 5)
print(f"Área del triángulo: {triangulo1.calcular_area()}")

cuadrado1 = Cuadrado(4)
print(f"Área del cuadrado: {cuadrado1.calcular_area()}")

lavadora1 = Lavadora("LG", "Turbowash", "A++", 15)
print(lavadora1.encender())
print(lavadora1.iniciar_ciclo())

refrigerador1 = Refrigerador("Samsung", "CoolMaster", "A++", True)
print(refrigerador1.encender())
print(refrigerador1.regular_temperatura())

admin1 = Administrador("admin", "1234")
admin1.iniciar_sesion("admin", "1234")
admin1.gestionar_usuarios()

cliente1 = Cliente("cliente1", "abcd")
cliente1.iniciar_sesion("cliente1", "abcd")
cliente1.realizar_compra()
   
