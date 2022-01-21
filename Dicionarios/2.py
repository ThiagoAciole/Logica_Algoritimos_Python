from random import randint
from time import sleep
from operator import itemgetter
jogo={"jogador1": randint(1,6),
"jogador2": randint(1,6),
"jogador3": randint(1,6),
"jogador4": randint(1,6),
"jogador5": randint(1,6),
}
ranking=[]
print("-="*30)
print("                 VALORES SORTEADOS           ")
print("-="*30)
for k, v in jogo.items():
    print(f" =>{k} tirou {v} dado.")
    sleep(0.5)
ranking=sorted(jogo.items(), key=itemgetter(1), reverse=True)
print("-="*30)
print("== RANKING DOS JOGADORES ==")
for i, v in enumerate(ranking):
    print(f"    {i+1}° Lugar: {v[0]} com {v[1]}")
    sleep(0.5)