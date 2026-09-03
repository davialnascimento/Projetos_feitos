#pedir uma senha repetidamente usando while até atender todos os critérios
#sendo eles: ter  8 caracteres, 1 maiúscula, 1 minúscula, 1 número e 1 especial
#A cada tentativa inválida, informe quais critérios faltaram.
print("insira uma senha com 8 caracteres, 1 maiúscula, 1 minúscula, 1 número e 1 especial ")
senha= input("insira uma senha: ")

while True:
    if len(senha) <8:
        print("numero de caracteres é inferior a quantidade mínima")
    elif senha.islower():
        print("ao menos uma letra maiúscula")
    elif senha.isalpha():
        print("é necessário ter um número")
    elif senha.isalnum():
        print("é necessário de um caractere especia")
    else:
        print ("senha válida")
        break
    senha=input("insira outra senha")

