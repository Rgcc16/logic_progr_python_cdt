##MVC
#Model
###tem que ter a aentrada dos numeros, tipo onde vou inserir os numeros, juntado os numeros utlizados e mandando para o controlador


#View
###Com os dados so vai produzir a visualização, resultado, o calculo feito, etc


#Controller
###Com os números em maos ele vai organizar e gerenciar o que deve ser feito, e azer contecer, mandando o que deve ser visualizado para o view
def mostrar_menu():
print("/n---calculadora---/n")
print("/n---adição---/n")
print("/n---Subtração---/n")
print("/n---Sair---/n")
print("/n------/n")

def obter_numeros():
    while True:
    try:
        num1 = float(input("Digite o primeiro Número"))
        num2 = float(input("digite o segundo Número"))
        return num1, num2
    exceptValueErro:
    print("Entrada Inválida, Por Favor, "/
          "digite números Validos")
    

main()