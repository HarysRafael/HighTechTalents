lista_cliente = []
dicionario_cliente = {}

def menu():
    print("")           
    print("Cadastro de Cliente")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
    print("")
    opcao = int(input("Digite a opção: "))
    print("")
    return opcao

def cadastrar_cliente():
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")            
    verifica_campos(nome, telefone, email)
    adiciona_cliente(nome, telefone, email, lista_cliente, dicionario_cliente)                             
    
def verifica_campos(nome, telefone, email):
    if(nome == "" or telefone == "" or email == ""):
        print("")
        print("É preciso preencher todos os campos!")    

def adiciona_cliente(nome, telefone, email, lista_cliente, dicionario_cliente):
    dicionario_cliente = {"Nome" : nome, "Telefone" : telefone, "E-mail" : email}
    lista_cliente.append(dicionario_cliente)                     
                
def confere_lista(lista_cliente):
    if(len(lista_cliente)<1):
        print("Não há clientes na lista!")                    
                               
def imprime_lista(lista_cliente):                
    for item in lista_cliente:
       print(item)           
    
def fechar_programa():
    print("Até logo!")

def excecao_opcao_invalida():
    print("Opção inválida")                      
            
while True:    
    opcao = menu() 
    
    if opcao in [1,2,3]:
        if(opcao == 1):
            cadastrar_cliente()
                                    
        elif (opcao == 2):
            confere_lista(lista_cliente)                                                         
            imprime_lista(lista_cliente) 
            
        elif(opcao == 3):
            fechar_programa
            break                   
        
    else:
        excecao_opcao_invalida();

            
