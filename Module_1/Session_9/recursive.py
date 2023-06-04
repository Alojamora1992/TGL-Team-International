import sys
sys.setrecursionlimit(34000)

def factorial(n):
    #caso base
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
def sumatoria(n):
    #caso base
    if n== 0:
        return 0
    else:
        return n + sumatoria(n-1)
    
def reverse(string):
    
    if string: 
        return string[-1] + reverse[:-1]    
    else:
        #caso base
        return ""
def fib(n):
    if n == 1 or n ==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def hanoi (disks: int, source:int, helper: int, target: int):
    if disks == 1:
        print(f"Paso: Mover ficha de {source} -> {target}")
    else:
        hanoi(disks -1, source =  source, helper = target, target = helper)
        print(f"Paso: Mover ficha de {source} -> {target}")
        hanoi(disks -1, source =  helper, helper = source, target = target)

print(hanoi(4, source = 1, helper = 2, target = 3))