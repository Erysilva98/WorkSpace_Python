print ('\nAtividade 14/03 - Erimilson Silva')
print('\nQ6 - Forma um triângulo retângulo ? ')

print("Informe 3 Números Inteiro e veja se forma o Teorema de Pitágoras")

lado1 = int (input ("DIGITE NÚMERO DO LADO A: ")) 
lado2 = int (input ("DIGITE NÚMERO DO LADO B: "))
lado3 = int (input ("DIGITE NÚMERO DO LADO C: "))

a = lado1 * lado1
b = lado2 * lado2
c = lado3 * lado3

if (c == a + b):
    print("\n Os Números Digitados Forma o Triângulo Retângulo.")
else:
   print("\n Os Números não Forma o Triângulo Retângulo.")
