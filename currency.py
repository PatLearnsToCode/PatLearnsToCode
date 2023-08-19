#Hi ho
def currency (usdollars):
    return round((usdollars),2)

def php(pesos):
    return (pesos*0.018 )

def soles(soles_value):
    return (soles_value*0.27)

def reais(reais):
    return (reais*0.20)

a = float(input("What do you have left in pesos? "))
b = float(input("What do you have left in soles?  "))
c = float(input("What do you have left in reais?  "))

pesos = php(a) 
soles1 = soles(b)
reais1 = reais(c)

currency_total = pesos+soles1+reais1
usdollars = currency_total

USDollars = currency(usdollars)
print("USD value in total:", USDollars, "$")


