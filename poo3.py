class Empleado:
    nombre= str
    salario = float
    departamento = str
    equipo = list
    
    def __init__(self, nombre: str, salario: float, departamento: str):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento
    
    def trabajar(self):
        return f"{self.nombre} está trabajando en {self.departamento}."

class Gerente(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, equipo: list):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo
    
    def supervisar_equipo(self):
        return f"{self.nombre} está supervisando a su equipo."

class Desarrollador(Empleado):
    def __init__(self, nombre: str, salario: float, departamento: str, lenguaje: str):
        super().__init__(nombre, salario, departamento)
        self.lenguaje = lenguaje
    
    def escribir_codigo(self):
        return f"{self.nombre} está escribiendo código en {self.lenguaje}."

class FiguraGeometrica:
    def calcular_area(self):
        pass

class Triangulo(FiguraGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.lado = lado
    
    def calcular_area(self):
        return self.lado ** 2

class Electrodomestico:
    def __init__(self, marca: str, modelo: str, consumo: str):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo
    
    def encender(self):
        return f"{self.marca} {self.modelo} está encendido."

class Lavadora(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumo: str, capacidad: float):
        super().__init__(marca, modelo, consumo)
        self.capacidad = capacidad
    
    def iniciar_ciclo(self):
        return f"Lavadora {self.marca} iniciando ciclo de lavado."

class Refrigerador(Electrodomestico):
    def __init__(self, marca: str, modelo: str, consumo: str, tiene_congelador: bool):
        super().__init__(marca, modelo, consumo)
        self.tiene_congelador = tiene_congelador
    
    def regular_temperatura(self):
        return f"Regulando temperatura del refrigerador {self.marca}."

class Usuario:
    def __init__(self, nombre_usuario: str, contrasena: str):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
    
    def iniciar_sesion(self, usuario: str, contrasena: str):
        return self.nombre_usuario == usuario and self.contrasena == contrasena

class Administrador(Usuario):
    def gestionar_usuarios(self):
        return "Gestionando usuarios del sistema."

class Cliente(Usuario):
    def realizar_compra(self):
        return "Realizando una compra en la tienda online."
    
    
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
print(f"Inicio de sesión: {admin1.iniciar_sesion('admin', '1234')}")
print(admin1.gestionar_usuarios())

cliente1 = Cliente("cliente1", "abcd")
print(f"Inicio de sesión: {cliente1.iniciar_sesion('cliente1', 'abcd')}")
print(cliente1.realizar_compra())
   
