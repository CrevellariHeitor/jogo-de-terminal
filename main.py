class Personagem: 
    def __init__(self, nome, vida, ataque, defesa): 
        self.nome = nome 
        self._vida = vida
        self.ataque = ataque 
        self.defesa = defesa 
        
    def atacar(self, alvo): 
        dano = max(0, self.ataque - alvo.defesa) # max(0) para o dano não ser negativo caso a defesa seja maior que o ataque
        alvo.receber_dano(dano) 
        return f'{self.nome} causou {dano} de dano!'
        
    def receber_dano(self, dano): 
        self._vida = max(0, self._vida - dano) # mesma coisa sobre omax(0) no dano
        
    def esta_vivo(self): 
        return self._vida > 0 
    
    def str(self): 
        return f'{self.nome} - Vida: {self._vida}'
    
class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=25, defesa=15) # o super() aproveita todos os atributos do pai (personagem)
        self.energia = 50

    def espada(self, alvo):
        if self.energia >= 20:
            dano = max(0, (self.ataque * 2) - alvo.defesa)
            alvo.receber_dano(dano)
            self.energia -= 20
            return f'{self.nome} te deu um golpe de espada e causou {dano} de dano!'
        return f'{self.nome} não tem energia o suficiente!'
    
class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=70, ataque=15, defesa=8)
        self.mana = 100 

    def bola_de_fogo(self, alvo):
        if self.mana >= 30:
            dano = max(0, (self.ataque * 3) - alvo.defesa)
            alvo.receber_dano(dano)
            self.mana -= 30
            return f'{self.nome} usou bola de fogo e causou {dano} de dano!'
        return f'Não tem mana o suficiente!'

class Inimigo(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=50, ataque=10, defesa=15)

def batalha(heroi, vilao):
    turno = 1

    while heroi.esta_vivo() and vilao.esta_vivo():

        print(heroi)
        print(vilao)

        opcoes = {'1': 'Ataque', '2': 'Habilidade especial'}

        if isinstance(heroi, Guerreiro):
            opcoes['2'] = f'Golpe de Espada (Energia: {heroi.energia})'
        elif isinstance(heroi, Mago):
            opcoes['2'] = f'Bola de Fogo (Mana: {heroi.mana})'

        print('\nO que deseja fazer?')
        for key, value in opcoes.items():
            print(f' {key} - {value}')

        acao = ''
        while acao not in opcoes:
            acao = input('\nEscolha uma ação: ')
            if acao not in opcoes:
                print(f'Digite uma opção válida. {list(opcoes.keys())}')

        print('\n-- Ação do Herói --')
        if acao == '1':
            resultado = heroi.atacar(vilao)
        elif acao == '2':
            if isinstance(heroi, Guerreiro):
                resultado = heroi.espada(vilao)
            elif isinstance(heroi, Mago):
                resultado = heroi.bola_de_fogo(vilao)
        print(resultado)

        if not vilao.esta_vivo():
            break

        print('\n-- Ação do Vilão --')
        resultado_vilao = vilao.atacar(heroi)
        print(resultado_vilao)

        turno += 1

    print('\n===== FIM DA BATALHA =====')
    if heroi.esta_vivo():
        print(f' {heroi.nome} venceu a batalha!')
    else:
        print(f' {heroi.nome} foi derrotado...')



guerreiro = Guerreiro('Heitor')
inimigo = Inimigo('Satanás')
batalha(guerreiro, inimigo)
