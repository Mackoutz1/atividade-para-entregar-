print("Bem-Vindo , o cinema é aberto das 13:00 ás 23:30, fique a vontade")
d = int(input("Dia da semana: "))
h = int(input("Hora do inicio da sessão: "))
m = int(input("Minuto de início da sessão: "))
if h>=23 and m>30 or h<13:
    print("O cinema já fechou!")
e = input("Estudante: ") #essa linha receberá um caractere sendo S caso o cliente seja estudante, ou um caractere N caso nao seja estudante
metodo_pagamento = input("Método de pagamento: ")
preco = float()
desconto = float()
ingresso = float()
if d == 1:
   if h>=13 and h<=18 and m<=30 or m>=30:
      preco = 30.00
      if e == "N" :
       if metodo_pagamento == "C":
        desconto = preco * 0.30
        ingresso = preco - desconto
       else:
        ingresso = preco
      elif e == "S":
       ingresso = preco/2
      else:
       ingresso = preco
   else:
    preco = 30.00
    if e == "N":
      if metodo_pagamento == "C":
        desconto = preco * 0.30
        ingresso = preco - desconto
      else:
        ingresso = preco
    elif e == "S":
      ingresso = preco /2
    else:
      ingresso = preco
elif d == 2 or d == 3:
   if h<=18 and m<=30 or m>=30:
     preco = 15.00
     if e == "N":
       if metodo_pagamento == "C":
        desconto = preco * 0.50
        ingresso = preco - desconto
       else:
        ingresso = preco
     elif e == "S":
       ingresso = preco /2
     else:
       ingresso = preco
   else:
     preco = 20.00
     if e == "N":
       if metodo_pagamento == "C":
         desconto = preco * 0.50
         ingresso = preco - desconto
       else:
         ingresso = preco
     elif e == "S":
         ingresso = preco/2
     else:
         ingresso = preco
elif d == 4:
   if h<=18 and m<=30 or m>=30:
     preco = 15.00
     if e == "N":
       if metodo_pagamento == "C":
        desconto = preco * 0.50
        ingresso = preco - desconto
       else:
        ingresso = preco
     elif e == "S":
       ingresso = preco /2
     else:
       ingresso = preco
   else:
     preco = 30.00
     if e == "N":
       if metodo_pagamento == "C":
         desconto = preco * 0.50
         ingresso = preco - desconto
       else:
         ingresso = preco
     elif e == "S":
         ingresso = preco/2
     else:
         ingresso = preco
elif d == 5:
   if h<=18 and m<=30 or m>=30:
     preco = 20.00
     if e == "N":
       if metodo_pagamento == "C":
        desconto = preco * 0.50
        ingresso = preco - desconto
       else:
        ingresso = preco
     elif e == "S":
       ingresso = preco /2
     else:
       ingresso = preco
   else:
     preco = 30.00
     if e == "N":
       if metodo_pagamento == "C":
         desconto = preco * 0.50
         ingresso = preco - desconto
       else:
         ingresso = preco
     elif e == "S":
         ingresso = preco/2
     else:
         ingresso = preco
elif d == 6:
   if h<=18 and m<=30 or m>=30:
     preco = 20.00
     if e == "N":
       if metodo_pagamento == "C":
        desconto = preco * 0.50
        ingresso = preco - desconto
       else:
        ingresso = preco
     elif e == "S":
       ingresso = preco /2
     else:
       ingresso = preco
   else:
     preco = 40.00
     if e == "N":
       if metodo_pagamento == "C":
         desconto = preco * 0.30
         ingresso = preco - desconto
       else:
         ingresso = preco
     elif e == "S":
         ingresso = preco/2
     else:
         ingresso = preco
elif d == 7:
   if h<=18 and m<=30 or m>=30:
     preco = 30.00
     if e == "N":
       if metodo_pagamento == "C":
        desconto = preco * 0.20
        ingresso = preco - desconto
       else:
        ingresso = preco
     elif e == "S":
       ingresso = preco /2
     else:
       ingresso = preco
   else:
     preco = 40.00
     if e == "N":
       if metodo_pagamento == "C":
         desconto = preco * 0.20
         ingresso = preco - desconto
       else:
         ingresso = preco
     elif e == "S":
         ingresso = preco/2
     else:
         ingresso = preco
print('Valor do ingresso: R$', format(ingresso,'.2f'))
