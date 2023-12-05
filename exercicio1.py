from random import choice

lista_de_opcoes = ["pe", "pa", "te"]
count1 = 0
count2 = 0
    
def ChecaGanhador (vitorias1:int, vitorias2:int):
    if vitorias1 > vitorias2:
        return "Você ganhou o jogo no melhor de 3!"
    elif vitorias1 < vitorias2:
        return "Você perdeu o jogo no melhor de 3!"
    else:
        return "Partida empatada no melhor de 3!"
    
while True:        
    for i in range(1,4):
        escolha_user = str(input("Digite a opção do cochete >>> [pe]-Pedra | [pa]-Papel | [te]-Tesoura >>>> ")).lower()
        escolha_pc = choice(lista_de_opcoes)

        if   escolha_user == "pe" and escolha_pc == "pe":
            print(f"Pedra-{escolha_user} X Pedra-{escolha_pc} = Empate")
            count1 += 1
            count2 += 1

        elif escolha_user == "pe" and escolha_pc == "pa":
            print(f"Pedra-{escolha_user} X Papel-{escolha_pc} = Vc perdeu!")
            count2 += 1

        elif escolha_user == "pe" and escolha_pc == "te":
            print(f"Pedra-{escolha_user} X Tesoura{escolha_pc} = Vc ganhou!")
            count1 += 1

        elif escolha_user == "pa" and escolha_pc == "pe":
            print(f"Papel-{escolha_user} X Pedra-{escolha_pc} = Vc ganhou!")
            count1 += 1

        elif escolha_user == "pa" and escolha_pc == "pa":
            print(f"Papel-{escolha_user} X Papel-{escolha_pc} = Empate")
            count1 += 1
            count2 += 1

        elif escolha_user == "pa" and escolha_pc == "te":
            print(f"Papel-{escolha_user} X Tesoura-{escolha_pc} = Vc perdeu!")
            count2 += 1

        elif escolha_user == "te" and escolha_pc == "pe":
            print(f"Tesoura-{escolha_user} X Pedra-{escolha_pc} = Vc perdeu!")
            count2 += 1

        elif escolha_user == "te" and escolha_pc == "pa":
            print(f"Tesoura-{escolha_user} X Papel-{escolha_pc} = Vc ganhou!")
            count1 += 1

        elif escolha_user == "te" and escolha_pc == "te":
            print(f"Tesoura-{escolha_user} X Tesoura-{escolha_pc} = Empate")
            count1 += 1
            count2 += 1

    print(ChecaGanhador(count1,count2))
