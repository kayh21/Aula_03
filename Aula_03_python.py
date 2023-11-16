# Estruturas Condicionais:
# As estruturas condicionais permitem que um programa execute diferentes comandos de acordo com as condições estabelecidas
# 1°: O Comando if:  Significa "SE", avaliando se a expressão é verdadeira
# 2°: O Comando elif: O comando elif é usado para testar múltiplas condições em sequência. Ele só é
# avaliado se as condições anteriores forem falsas. A sintaxe é a seguinte:
# if #expressao_booleana1:           
#   # Bloco de código a ser executado se a expressão 1 for verdadeira
# elif #expressao_booleana2:
#   # Bloco de código a ser executado se a expressão 1 não for verdadeira e 2 for verdadeira
# else:
    # Bloco de código a ser executado se nenhuma expressão for verdadeira
    
nota = 85
if nota >= 90:
    print("Ótimo desempenho!")
elif nota >= 70:
    print("Bom desempenho.")
else:
    print("Melhorar na próxima.")
    
# 3°: O Comando else: O comando else é usado para definir um bloco de código a ser executado quando 
# todas as condições anteriores forem falsas. Ele não tem uma expressão booleana associada, 
# pois é o último caso a ser considerado quando nenhum dos casos anteriores for verdadeiro.

numero = 7
if numero % 2 == 1:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 4°: NOT é usado como negação junto do IF, exemplo: tudo que não for par, ou seja é um impar

language  =  "Inglês"    

if not language  == "Português":
   print("Contratado ")
else: 
   print("Não selecionado")

#Exercício 01: Crie um programa para efetuar a leitura de um número inteiro e apresentar o resultado do quadrado deste número.
n1 = int(input("Digite um número\n"))
print("Esse é o resultado do quadrado do numero que você digitou:", n1 * n1)

#Exercício 02: Crie duas variáveis para armazenar seu primeiro nome e sobrenome. Em seguida, concatene-as para formar seu nome completo e exiba o resultado.
nome = input("Digite seu nome\n")
sobrenome = input("Digite seu sobrenome\n")
print("Então o seu nome completo é", nome, sobrenome, "?")

#Exercício 03: Peça ao usuário para digitar dois números inteiros e armazene-os em variáveis. Realize a concatenação desses números como strings e exiba o resultado.
numero01 = input("Digite o seu numero favorito\n")
numero02 = input("Digite a sua idade\n")
print("o seu numero favorito e a sua idade são", numero01, "e", numero02)

#Exercício 04: Crie uma variável para armazenar a palavra "Python". Em seguida, adicione um número inteiro ao final da palavra usando a concatenação e exiba o resultado.
codigo = "Python"
versao = input("Digite uma versão do python\n")
print(codigo + versao)

#Exercício 05: Declare uma variável contendo uma frase. Em seguida, peça ao usuário para digitar uma palavra e concatene essa palavra no final da frase. Exiba o resultado.
frase = "as rosas são vermelhas e as violetas são"
complete = input("complete o ditado: as rosas são vermelhas e as violetas são\n")
print(f"a frase criada foi: {frase} {complete}")

#Exercício 06: Crie três variáveis para armazenar a quantidade de horas, minutos e segundos. Concatene esses valores para formar uma mensagem de tempo no formato "hh:mm:ss".
horas = int(input("digite a hora\n"))
minutos = int(input("Digite os minutos\n"))
segundos = int(input("Digite os segundos\n"))
print(f"agora são: {horas}hh:{minutos}mm:{segundos}ss")

#Exercício 07: Declare duas variáveis com números de telefone, incluindo um código de área e o número principal. Concatene esses valores para formar um número de telefone completo.
celular = int(input("Digite o seu número de celular sem o ddd\n"))
ddd = int(input("Agora digite o ddd de onde é o seu número de celular\n"))
print(f"Confere se anotei o seu número certo: {ddd}{celular}")

#Exercício 08: Crie uma lista de ingredientes para uma receita. Use concatenação para formar uma única string que liste os ingredientes separados por vírgulas.
ingrediente1 = str(input("Digite o primeiro ingrediente\n"))
ingrediente2 = str(input("Digite o segundo ingrediente\n"))
ingrediente3 = str(input("Digite o terceiro ingrediente\n"))
print(f"os itens da receita são: {ingrediente1}, {ingrediente2} e {ingrediente3}")

#Exercício 09: Peça ao usuário para digitar três adjetivos e armazene-os em variáveis. Em seguida, use essas palavras para criar uma frase concatenada que descreve algo interessante.
adjetivo1 = input("Digite um elogio sobre você\n")
adjetivo2 = input("Digite outro elogio sobre sua mãe\n")
adjetivo3 = input("Digite mais um elogio sobre seu pai\n")
print(f"Eu me acho {adjetivo1}, acho minha mãe {adjetivo2} e acho meu pai {adjetivo3}")

if numero == 10:
   print(f"o número é {numero}")
else:
   print(f"Opa é {numero}")

# == igual 
# != diferente
# > maior
# < menor
# else = senão 
# if = se
# and = e
# or = ou
# for = para
# while = enquanto
# not = não 

# senha_digitada = input("Digite uma senha")
# nome = input("Digite seu nome")
# senha = "1234"
# if senha == senha_digitada and nome == "Kayllane":
#    print("Acesso permitido")
# else:
#    print(f"Acesso negado, você digitou {senha_digitada} ou {nome} incorreto")

#Execício 10: Crie uma condição para comparar idades: 45 e 18 -  QUAL É MENOR E QUAL É MAIOR?
idade1 = 45 
idade2 = 18
if (idade1 > idade2):
   print("45 é maior que 18")
else:
   print("Essa informação é falsa, pois 45 é sim maior que 18")

#Execício 11: Crie um sistema para permitir a verificação de menores em um show
menor_de_idade = int(input("digite sua idade\n"))
maior_de_idade = 18 
if (menor_de_idade < maior_de_idade):
   print("Entrada negada no show")
else:
   print("Entrada permitida no show")

#Exercício 12: Crie um algoritmo que permita a entrada de 3 notas de alunos, utilize o bloco de código if() para verificar se o aluno passou.
nota_da_Ana = float(input("Digite a media final da nota da Ana\n"))
nota_da_Rafa = float(input("Digite a media final da nota da Rafa\n"))
media = 6

if(nota_da_Ana < media):
   print("Ana infelizmente reprovou")
else:
   print("Ana passou, parabéns")

if(nota_da_Rafa < media):
   print("Rafa infelizmente reprovou")
else:
   print("Rafa passou, parabéns")

#Bloco de estrutura
# Class (Self
#       def __init__(Self)
#           if 2 == 2:
#              print("É igual")
#           else: 
#              print("É diferente")
# 
# 