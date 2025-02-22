#factorial usando for
# num = 5
# total: int


# def factorial(n:int) -> int:
#     res: int = 1
#     for i in range(1,n+1):
#         res = res*i
#     return res

# print(factorial(num))

#factorial usando while

# num = 5
# total: int


# def factorial(n:int) -> int:
#     res: int = 1
#     cont = 1
#     while cont in range(n+1):
#         res = res*cont
#         cont += 1
#     return res

# print(factorial(num))

#ejercicicio recursion

# num = 5

# def factorial(n)-> int:
#     if n == 1:
#         return n
#     return factorial(n - 1 )*n
# print(factorial(5))

#ejercicio tarea

# def fibonaccio(n:int)->int:
#     if n <= 1:
#         return n
#     return fibonaccio(n-1) + fibonaccio(n-2)

# for i in range(7):
#     print(fibonaccio(i),end=" ") 
    
#ejercicio 2

# def sumar(lista):
#     if len(lista) == 1:
#         print(lista[0])
#         return lista[0]
#     return lista[0] + sumar(lista[1:])

# num = []
# nums = 0
# for n in range (5):
#     num.append (int(input("digite los numeros:")))
# print(sumar(num))

#ejercicio 3

# def multiply(a,b):
#     if b == 1:
#         return a
#     return a + multiply(a,b-1)

# print(multiply(5,3))

#ejercicio 4

def divide(a,b):
    if a < b:
        return 0
    return 1 + divide(a-b,b)

print(divide(4,2))
  


