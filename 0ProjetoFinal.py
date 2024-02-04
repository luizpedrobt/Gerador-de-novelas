from random import randint
import os

class Personagem:
    def __init__(self, genero):
        self.genero = genero
        self.nome = ""
        self.sobrenome = escolheDeLista(lsobrenomes)
        self.completar()
    def completar(self):
        if self.genero == True:
            self.nome = escolheDeLista(lnome_feminino)
        else:
            self.nome = escolheDeLista(lnome_masculino)
    def __str__ (self):
        return (f"{self.nome.strip()} {self.sobrenome.strip()}")
    
def escolheDeLista(lista):
    return lista[randint(0, len(lista)-1)]

with open("nomes_femininos.txt", "r", encoding='utf-8') as nf:
    lnome_feminino = list(nf.readlines())
with open("nomes_masculinos.txt", "r", encoding='utf-8') as nm:
    lnome_masculino = list(nm.readlines())
with open("acoes.txt", "r", encoding='utf-8') as acoes:
    lacoes = list(acoes.readlines())
with open("locais.txt", "r", encoding='utf-8') as locais:
    llocais = list(locais.readlines())
with open("sobrenomes.txt", "r", encoding='utf-8') as sobrenomes:
    lsobrenomes = list(sobrenomes.readlines())
with open("finais_protagonista.txt", "r", encoding='utf-8') as finais_prot:
    lfinais_prot = list(finais_prot.readlines())
with open("finais_viloes.txt", "r", encoding='utf-8') as finais_viloes:
    lfinais_viloes = list(finais_viloes.readlines())

lista_protagonistas = list()
lista_coadjuvantes = list()
lista_viloes = list()

os.system('cls')
nome_da_novela = input('Qual será o nome da sua novela? ')
os.system('cls')

capitulos = int(input('Quantos capítulos terá a sua novela? '))
os.system('cls')

protagonistas = int(input('Quantos protagonistas terão a sua história? O número precisa ser par: ')) 
os.system('cls')
while protagonistas % 2 !=0:
    protagonistas = int(input('O número deve ser par! '))
    os.system('cls')
    
for i in range(protagonistas // 2):
    p_masc = Personagem(False)
    p_fem = Personagem(True)
    lista_protagonistas.append(p_fem)
    lista_protagonistas.append(p_masc)
    
viloes = int(input('Quantos viloes terão a sua história? O número precisa ser par: '))
os.system('cls')
while viloes % 2 !=0:
    viloes = int(input('O número deve ser par! '))
    os.system('cls')
    
for i in range(viloes // 2):
    v_masc = Personagem(False)
    v_fem = Personagem(True)
    lista_viloes.append(v_fem)
    lista_viloes.append(v_masc)
    
coadjuvantes = int(input('Quantos coadjuvantes terão a sua história? O número precisa ser par: '))
os.system('cls')
while coadjuvantes % 2 !=0:
    coadjuvantes = int(input('O número deve ser par! '))
    os.system('cls')
    
for i in range(coadjuvantes // 2):
    c_masc = Personagem(False)
    c_fem = Personagem(True)
    lista_coadjuvantes.append(c_fem)
    lista_coadjuvantes.append(c_masc)
    
print(f'***{nome_da_novela.upper()}***')

print('')

print('PROTAGONISTAS')
print('='*20)   
for i in lista_protagonistas:
    print(i)
    
print('')

print('VILÕES')  
print('='*20)  
for i in lista_viloes:
    print(i)
    
print('')

print('COADJUVANTES')
print('='*20)
for i in lista_coadjuvantes:
    print(i)
 
lista_impressaoA1 = []
lista_impressaoB1 = []
lista_impressaoC1 = []
lista_impressaoA2 = []
lista_impressaoB2 = []
lista_impressaoC2 = []
lista_impressaoF1 = []
lista_impressaoF2 = []

print('')
    
for capitulo in range(capitulos):
    
    print('')
    print(f'Episódio {capitulo + 1}')
    print('='*20)
    print('')
    
    for parametro in range(len(lista_protagonistas)):

        #(b)
        protagonista_usado = escolheDeLista(lista_protagonistas)
        coadjuvante_usado = escolheDeLista(lista_coadjuvantes)
        a1 = (f'{protagonista_usado.nome.strip()} {escolheDeLista(lacoes).strip()}')
        if protagonista_usado.genero == True:
            a1 = a1.replace("@", "a")
        else:
            a1 = a1.replace("@", "o")
        a2 = (f'{coadjuvante_usado.nome.strip()} {escolheDeLista(llocais).strip()}')
        if coadjuvante_usado.genero == True:
            a2 = a2.replace("@", "a")
        else:
            a2 = a2.replace("@", "o")
        print(a1 + " " + a2)
        lista_impressaoA1.append(a1)
        lista_impressaoA2.append(a2)

        #(c)
        protagonista_usado = escolheDeLista(lista_protagonistas)
        vilao_usado = escolheDeLista(lista_viloes)
        b1 = (f'{vilao_usado.nome.strip()} {escolheDeLista(lacoes).strip()}')
        if vilao_usado.genero == True:
            b1 = b1.replace("@", "a")
        else:
            b1 = b1.replace("@", "o")
        b2 = (f'{protagonista_usado.nome.strip()} {escolheDeLista(llocais).strip()}')
        if protagonista_usado.genero == True:
            b2 = b2.replace("@", "a")
        else:
            b2 = b2.replace("@", "o")
        print(b1 + " " + b2)
        lista_impressaoB1.append(b1)
        lista_impressaoB2.append(b2)

        #(d)
        protagonista_usado = escolheDeLista(lista_protagonistas)
        vilao_usado = escolheDeLista(lista_viloes)
        c1 = (f'{protagonista_usado.nome.strip()} {escolheDeLista(lacoes).strip()}')
        if protagonista_usado.genero == True:
            c1 = c1.replace("@", "a")
        else:
            c1 = c1.replace("@", "o")
        c2 = (f'{vilao_usado.nome.strip()} {escolheDeLista(llocais).strip()}')
        if vilao_usado.genero == True:
            c2 = c2.replace("@", "a")
        else:
            c2 = c2.replace("@", "o")
        print(c1 + " " + c2)
        lista_impressaoC1.append(c1)
        lista_impressaoC2.append(c2)
        
print('')
print('Episódio Final')
print(20*'=')
print('')
for parametro in range(len(lista_viloes)):
    vilao_usado = escolheDeLista(lista_viloes)
    protagonista_usado = escolheDeLista(lista_protagonistas)
    f1 = (f'{vilao_usado.nome.strip()} {escolheDeLista(lfinais_viloes).strip()}')
    if vilao_usado.genero == True:
        f1 = f1.replace("@", "a")
    else:
        f1 = f1.replace("@", "o")
    f1 = f1.replace("#", protagonista_usado.nome)
    lista_impressaoF1.append(f1)

    print(f1)

for parametro in range(len(lista_protagonistas)):
    protagonista_usado = escolheDeLista(lista_protagonistas)
    vilao_usado = escolheDeLista(lista_viloes)
    f2 = (f'{protagonista_usado.nome.strip()} {escolheDeLista(lfinais_prot).strip()}')
    if protagonista_usado.genero == True:
        f2 = f2.replace("@", "a")
    else:
        f2 = f2.replace("@", "o")
    f2 = f2.replace("#", vilao_usado.nome.strip())
    lista_impressaoF2.append(f2)

    print(f2)

with open(f"Resenha_de_{nome_da_novela}.txt", "w", encoding='utf-8') as salvando_novela:
    salvando_novela.write(f"***{nome_da_novela.upper()}***\n")
    salvando_novela.write("\n")
    salvando_novela.write("PROTAGONISTAS\n")
    salvando_novela.write("="*20)
    salvando_novela.write("\n")
    for i in (lista_protagonistas):
        salvando_novela.write(i.__str__() + "\n")
    salvando_novela.write("\n")
    salvando_novela.write('VILÕES\n')
    salvando_novela.write("="*20)
    salvando_novela.write("\n")
    for i in (lista_viloes):
        salvando_novela.write(i.__str__() + "\n")
    salvando_novela.write("\n")
    salvando_novela.write('COADJUVANTES\n')
    salvando_novela.write("="*20)
    salvando_novela.write("\n")
    for i in (lista_coadjuvantes):
        salvando_novela.write(i.__str__() + "\n")
    controle = 0
    salvando_novela.write("\n")
    for capitulo in range(capitulos): 
        j = 0
        salvando_novela.write(f"Episódio {capitulo + 1}\n")
        salvando_novela.write('='*20)
        salvando_novela.write("\n")
        salvando_novela.write("\n")
        j = j+controle

        for i in range(len(lista_protagonistas)):
            salvando_novela.write(lista_impressaoA1[i+j] + " " + lista_impressaoA2[i+j] + "\n")
            salvando_novela.write(lista_impressaoB1[i+j] + " " + lista_impressaoB2[i+j] + "\n")
            salvando_novela.write(lista_impressaoC1[i+j] + " " + lista_impressaoC2[i+j] + "\n")
            controle = controle + 1
        salvando_novela.write("\n")

    salvando_novela.write("Episódio Final\n")
    salvando_novela.write('='*20)
    salvando_novela.write("\n")
    salvando_novela.write("\n")

    for i in range(len(lista_protagonistas)):
        salvando_novela.write(lista_impressaoF1[i] + "\n")
    for i in range(len(lista_protagonistas)):
        salvando_novela.write(lista_impressaoF2[i] + "\n")
    salvando_novela.write("\n")
    salvando_novela.write("===\n")
    salvando_novela.write(f"Arquivo <Resenha_de_{nome_da_novela}.txt> salvo com sucesso!")

print("")
print("===")
print(f"Arquivo <Resenha_de_{nome_da_novela}.txt> salvo com sucesso!")