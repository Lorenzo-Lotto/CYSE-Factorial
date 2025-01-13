x=int(input("inserisci il numero: "))
result=1
i=0
def fattoriale(x):
    if x==0:
        return 1
    else:
        return x*fattoriale(x-1)
print(fattoriale(x))