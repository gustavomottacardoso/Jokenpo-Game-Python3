import random
import time

print("\033[1;100mDesafio 045\033[m")
print(" ")

jogo = int(input("\033[1;94mEscolha:\033[m  "
      "\033[1;30;1m\n [ 1 ] PEDRA "
      "\n [ 2 ] TESOURA  "
      "\n [ 3 ] PAPEL\n \033[m"))

itens = ("Pedra", "Papel", "Tesoura")
computador = random.randint(1, 3)

print("\033[1;30;1m JO\033[m")
time.sleep(1)
print("\033[1;30;1m KEN\033[m")
time.sleep(1)
print("\033[1;30;1m PO\033[m")
time.sleep(1)
print(" ")



if jogo != computador:
    if jogo == 1 and computador == 2:
        print("\033[1;30;1m Eu escolhi tesoura e você pedra,\033[m \033[1;32mparabéns! \033[m")
    elif jogo == 1 and computador == 3:
        print("\033[1;30;1m Eu escolhi papel e você pedra,\033[m \033[1;31mperdedor!\033[m")
    elif jogo == 2 and computador == 1:
        print("\033[1;30;1m Eu escolhi pedra e você tesoura,\033[m \033[1;31mperdedor!\033[m")
    elif jogo == 2 and computador == 3:
        print("\033[1;30;1m Eu escolhi papel e você tesoura,\033[m \033[1;32mparabéns!\033[m")
    elif jogo == 3 and computador == 1:
        print("\033[1;30;1m Eu escolhi pedra e você papel,\033[m \033[1;32mparabéns!\033[m")
    elif jogo == 3 and computador == 2:
        print("\033[1;30;1m Eu escolhi tesoura e você papel,\033[m \033[1;31mperdedor!\033[m")
elif jogo == computador:
    print("\033[1;30;1mEMPATE\033[m")
elif (jogo != 1) or (jogo != 2) or (jogo != 3):
    print("\033[1;30;1mEscolha inválida!\033[m")