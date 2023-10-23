#Funciones de la libreria de py
'''
#VALOR ABSOLUTO
x= -21
print(abs(x))

#CONVERSIÓN BINARIO
a = 0
print(bin(a))

#VALOR UNICODE
i = 160
print(chr(i))

# RETORNA COCIENTE Y RESTO
a,b = 14,4
c,r = divmod(a,b)
print(c,r)

# CONVIERTE UNA CADENA A N° FLOTANTE
s='23.25'
y = float(s)
print(y)

#CONVERSION HEXADECIMAL
r= 21
c= hex(r)
print(c)

#OBTENCION DE UNA CADENA
q = input('algo:' )
print(q)

# CONVIERTE A ENTERO
p= '1365'
o= int(p)
print(o)
#FUNCION LEN ( DEVUELVE LA LONGITUD DEL OBJETO)
t= 13,23,35
print(len(t))

#MAYOR
l ,n = 6,19
mayor = max(l,n)
print(mayor)

#MENOR
k,h = 56,78
menor = min(k,h)
print(menor)

#CONVERSIONA OCTAL
f=124
ñ = oct (f)
print(ñ)

#POTENCIA
d,j =2,3
z = pow(d,j)
print(z)

# RETORNA EL ENTERO UNICODE
g = '~'
w = ord(g)
print(w)'''

#Ejercicio 22 py
#Entradas
nombre = input('Porfavor ingrese su nombre :')
apellido = input('Porfavor ingrese su apellido: ')

print(apellido.lower()+'_'+nombre.lower()+'@tdf.edu.ar')