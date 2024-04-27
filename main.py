def add(x,y):
  return x + y

def sub(x,y):
  return x - y

def multi(x,y):
  return x * y

def div(x,y):
  return x / y
  

print("Selecione uma operação.")
print("1. adição")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")

escolha = input("Escolha uma operação (1/2/3/4)")

if escolha in ('1','2','3','4'):
  n1 = float(input("Digite um numero:  "))
  n2 = float(input("Escolha outro numero:   "))

  if escolha == '1':
    print(add(n1,n2))

  if escolha == '2':
    print(sub(n1,n2))

  if escolha == '3':
    print(multi(n1,n2))

  if escolha == '4':
    print(div(n1,n2))

  