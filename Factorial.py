x=int(input("inserisci il numero: "))
result=1
i=0
while i<x:
    result*=(x-i)
    i+=1
print("Il fattoriale di" , x , "è:", result)