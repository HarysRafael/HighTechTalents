def login():
    usuario = input("Digite seu nome: ")
    print(f"Seja bem vindo, {usuario}")
    
def menu():
    print("\n")
    print("*** Tabuada ***")
    print("1 - Multiplicar")
    print("2 - Sair")
    opcao = int(input("Escolha uma opção: "))
    print("\n")    
    return opcao
    
def multiplicar():
    for i in range(0,11):
        for j in range(0,11):
            print(f"{i} x {j} = {i*j}" )
        print("\n")
    print("Sucesso!")   
    print("\n")     
            
def fechar_programa():
    print("Saindo do sistema...")
    
def excecao_opcao_invalida():    
    print("Opção inválida.");
        
login()    
while True:
    opcao = menu()
    if opcao in [1,2 ]:
        if opcao == 1:       
            multiplicar()
        elif opcao == 2:
            fechar_programa()            
            break        
        else:
            excecao_opcao_invalida()            
            
