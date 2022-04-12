
class Transportes:
    
    def __init__(self, nome, tipo, cor, ano, tracao):
        self.nome = nome
        self.tipo = tipo
        self.cor = cor
        self.ano = ano
        self.tracao = tracao
    
    def ligar(self):
        return (f"Ligando o {self.tipo} {self.nome}")
    
    def sair(self):        
        return(f"O {self.tipo} {self.nome} está saindo.")   
    
    def passear(self):
        return(f"O {self.tipo} {self.nome} está passeando por aí...")     
    
    def retornar(self):
        return(f"O {self.tipo} {self.nome} está retornando...")
    
    def parar(self):
        return(f"Parando o {self.tipo} {self.nome}")
    
    def desligar(self):
        return(f"O {self.tipo} {self.nome} está sendo desligado")            
        
###  Transportes Terrestres  ###

class Terrestre(Transportes):
    def __init__(self, nome, tipo, cor, ano, tracao, portas):
        super().__init__(nome, tipo, cor, ano, tracao)                        
        self.portas = portas       

    def buzinar(self):
        return (f"BIBIIIIIIIIIIIIII")

###  Carro  ###
                        
class Carro(Terrestre):
    def __init__(self, nome, tipo, cor, ano, tracao, portas):
        super().__init__(nome, tipo, cor, ano, tracao, portas)
        
    def carregarPessoas(self):
        return(f'Carregando Pessoas ao seu destino final...')        
    
    def __str__(self):        
        return(
            f'Nome:{self.nome}\nTipo:{self.tipo}\nCor:{self.cor}\nAno:{self.ano}\nTração:{self.tracao}\nPortas:{self.portas}\n'
        )            

###  Caminhão  ###

class Caminhao(Terrestre):
    def __init__(self, nome, tipo, cor, ano, tracao, portas, eixo, carroceria):
        super().__init__(nome, tipo, cor, ano, tracao, portas)
        self.eixo = eixo
        self.carroceria = carroceria
    
    def transportarCargas(self):
        return(f'Transportando Cargas')        
    
    def __str__(self):        
        return(
            f'Nome:{self.nome}\nTipo:{self.tipo}\nCor:{self.cor}\nAno:{self.ano}\nTração:{self.tracao}\nPortas:{self.portas}\nEixo:{self.eixo}\nCarroceria{self.carroceria}\n'
        )            

###  Transportes Aquáticos  ###

class Aquatico(Transportes):
    def __init__(self, nome, tipo, cor, ano, tracao, tripulantes):
        super().__init__(nome, tipo, cor, ano, tracao)
        self.tripulantes = tripulantes
            
    def ancorar(self):
        return (f'Ancorar {self.tipo} {self.nome}')
    
    def desancorar(self):
        return (f'Desancorar {self.tipo} {self.nome}')
    
    def navegar(self):
        return (f'{self.tipo} {self.nome} navegando por aí...')
    
 
###  Remo  ###
    
class BarcoRemo(Aquatico):
    def __init__(self, nome, tipo, cor, ano, tracao, tripulantes, remos, mateira_prima):
        super().__init__(nome, tipo, cor, ano, tracao, tripulantes)
        self.remos = remos
        self.materia_prima = mateira_prima        
        
    def remar(self):
        return (f'Remando o (a) {self.tipo} {self.nome}')
    
    def __str__(self):        
        return(
            f'Nome:{self.nome}\nTipo:{self.tipo}\nCor:{self.cor}\nAno:{self.ano}\nTração:{self.tracao}\nRemos:{self.remos}\nMatéria Prima:{self.materia_prima}\nTripulantes{self.tripulantes}\n'
        )            

###  Barco Motor  ###

class BarcoMotor(Aquatico):
    def __init__(self, nome, tipo, cor, ano, tracao, tripulantes, cabine):
        super().__init__(nome, tipo, cor, ano, tracao, tripulantes)
        self.cabine = cabine

    def __str__(self):        
        return(
            f'Nome:{self.nome}\nTipo:{self.tipo}\nCor:{self.cor}\nAno:{self.ano}\nTração:{self.tracao}\nCabine:{self.cabine}\nTripulantes{self.tripulantes}\n'
        )                

###  Aéreo  ###

class Aereo(Transportes):
    def __init__(self, nome, tipo, cor, ano, tracao, carga_kg):
        super().__init__(nome, tipo, cor, ano, tracao)        
        self.carga_kg = carga_kg
    
    def levantar_voo(self):
        return(f'{self.tipo} {self.nome} preparando para levantar voo...')   
    
    def voando(self):
        return(f'Voando...')
    
    def aterrissar(self):
        return(f'{self.tipo} {self.nome} preparando para aterrissar...') 

### Avião ###

class Aviao(Aereo):
    def __init__(self, nome, tipo, cor, ano, tracao, carga_kg, trem_de_pouso):
        super().__init__(nome, tipo, cor, ano, tracao, carga_kg)
        self.trem_de_pouso = trem_de_pouso

    def impulsionar(self):
        return(f'Impulsionando {self.tipo} {self.nome} à velocidade máxima...')        
    
    def __str__(self):       
        return(
            f'Nome:{self.nome}\nTipo:{self.tipo}\nCor:{self.cor}\nAno:{self.ano}\nTração:{self.tracao}\nCarga:{self.carga_kg}Kg\nTrem de Pouso{self.trem_de_pouso}\n'
        )                

###  Helicóptero  ###
class Helicoptero(Aereo):
    def __init__(self, nome, tipo, cor, ano, tracao, carga_kg, rotor):
        super().__init__(nome, tipo, cor, ano, tracao, carga_kg)
        self.rotor = rotor

    def girar_rotor(self):
        return(f"Girando rotor do {self.tipo} {self.nome} à velocidade máxima.")
    
    def parar_rotor(self):
        return(f"Parando rotor do {self.tipo} {self.nome}...")

    def __str__(self):       
        return(
            f'Nome:{self.nome}\nTipo:{self.tipo}\nCor:{self.cor}\nAno:{self.ano}\nTração:{self.tracao}\nCarga:{self.carga_kg}Kg\nRotor{self.rotor}\n'
        )                
        

###  Instância Carro  ###

carro = Carro("Chevett", "Carro", "Vermelho", "1985", "Mecânica", "2")    
print(carro)    
print(carro.ligar())
print(carro.sair())
print(carro.buzinar())
print(carro.passear())
print(carro.carregarPessoas())
print(carro.retornar())
print(carro.parar())
print(carro.desligar(),'\n')

###  Instância Caminhão  ###

caminhao  = Caminhao("Scania", "Caminhão", "Amarelo", "1999", "Mecânica", "2", "Duplo", "Simples")    
print(caminhao)    
print(caminhao.ligar())
print(caminhao.sair())
print(caminhao.buzinar())
print(caminhao.passear())
print(caminhao.transportarCargas())
print(caminhao.retornar())
print(caminhao.parar())
print(caminhao.desligar(),"\n")

###  Instância Remo  ###        
        
remo = BarcoRemo("Iracema", "Jangada", "Marron", "2022", "Humana", "4", "Madeira", "4")
print(remo)
print(remo.desancorar())
print(remo.remar())
print(remo.navegar())
print(remo.retornar())
print(remo.ancorar(),'\n')

###  Instância Barco Motor  ###

motor = BarcoMotor("Cruizer 275", "Lancha", "Branca/Azul","2007", "Mecânica","20","Simples")
        
print(motor)
print(motor.ligar())
print(motor.desancorar())
print(motor.navegar())
print(motor.retornar())
print(motor.ancorar())
print(motor.desligar(),'\n')

###  Instância Avião  ###    

aviao = Aviao("747 Boeing", "Avião", "Branco", "1999", "Mecânica", "1000", "27")
print(aviao.ligar())
print(aviao.impulsionar())
print(aviao.levantar_voo())
print(aviao.passear())
print(aviao.retornar())
print(aviao.aterrissar())
print(aviao.parar())
print(aviao.desligar(),'\n')

###  Instância Helicóptero  ###

helicoptero = Helicoptero("RCASS","Helicoptero","Cinza","2018","Mecânica","300","Simples")
print(helicoptero)
print(helicoptero.ligar())
print(helicoptero.girar_rotor())
print(helicoptero.levantar_voo())
print(helicoptero.voando())
print(helicoptero.aterrissar())
print(helicoptero.parar_rotor())
print(helicoptero.desligar())   

