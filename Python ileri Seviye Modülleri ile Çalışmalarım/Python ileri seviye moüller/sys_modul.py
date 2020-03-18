import sys

def kok_bulma(a , b ,c):
    
    kok = a * b /c
    
    return kok

if len(sys.argv) == 4 :
    print(kok_bulma(int(sys.argv[1]) , int(sys.argv[2]) , int(sys.argv[3])))

else:

    sys.stderr.write("Lütfen 3 değer girin")
    sys.stderr.flush()