# Octavia Ramadhani
# NIM : F55123015
x= [5, 5, 10, 3, 2, 6, 7]
y1 = 4
y2 = 2

def heuristik_searching(x, y1, y2):
    if y1 in x: 
        return x.index(y1)
    elif y2 in x:
        return x.index(y2)
    else:
        return 0
    
output = heuristik_searching(x, y1, y2)
print("Output", output)