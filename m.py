
#print(table.readline() + '\n')

key = "SOLVECRYPTO"
flag = "UFJKXQZQUNB" 
key = input("Enter Key: ")
flag = input("Enter Data: ")

answer = "picoCTF{CRYPTOISFUN}" #lol

#getting just the table
def lol(i,z):
    j = 0
    

    while j < 26:
       
        if i[0][0][j] == key[z]:
            return j
            
        j = j + 1
       
    


    

def lol2(z):
   
    b = 0

    i = []
    table = open('table.txt', 'r')
    for a in table.readlines():
       
        b = b + 1
        if b > 2 and b < 29:
            c = a[4:]
            c = c.replace(' ','')
            i.append(c.replace('\n', '').split('\n'))

            d = c[lol(i,z)]
    

            
            g = flag[z]
            
            if d == g:
                h = c.split('\n ')
                h = h[0]
                table.close()
                return h[0]

                #print(f)
y = ''
for z in range(0, len(flag)):

    y = y + lol2(z)

print(y)
           
            
            
