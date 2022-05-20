print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ7 - Se forma um triângulo, é qual tipo: isósceles, equilátero ou escaleno. ')

print("Informe 3 Números Inteiro e veja se forma um Triângulo")

lado1 = int (input ("DIGITE NÚMERO DO LADO A: ")) 
lado2 = int (input ("DIGITE NÚMERO DO LADO B: "))
lado3 = int (input ("DIGITE NÚMERO DO LADO C: "))

a = lado1 
b = lado2 
c = lado3 

if ( a > (b + c )) or (b > ( a + c )) or (c > (a + b)):
   print("\n Os Números não Forma um Triângulo")

# AB == BC != AC
elif (a == b) and (b == c ) and (a != c):
    print("\n Os Números Digitados Forma o Triângulo Isósceles.") 

# AB != BC != AC
elif (a != b) and (b != c) and (a != c):
    print("\n Os Números Digitados Forma o Triângulo Escaleno.")

# AB == BC == AC
else:
   print("\n Os Números Digitados Forma o Triângulo Equilátero.")
   