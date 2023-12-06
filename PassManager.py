import csv
from tabulate import tabulate




col_names = ["SITE","LOGIN","SENHA"]

def addPass(site,nome,passe):
    #criar dicionario e adicionar valores
    passe_lista = []
    passe_lista.append(site)
    passe_lista.append(nome)
    passe_lista.append(passe)
    
    #Abrir ficheiro e adicionar valores
    with open ("passes.csv","a", encoding="UTF-8") as csv_file:
        write = csv.writer(csv_file)
        write.writerow(passe_lista)
        


def changePass():

    procurar = 1
   

    #Abrir ficheiro com as passwords e guardar numa lista
    rows = []

    with open ("passes.csv","r", encoding="UTF-8") as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
                rows.append(row)
                

    
    #print(rows)
    rows = [ele for ele in rows if ele != []]

    #print(rows)
    while procurar == 1:
         #Input para perguntar qual a passe a mudar
        alt = input("Indique qual a password que pretende alterar: ")
        for lista in rows:
            index_lista = rows.index(lista)
            for ele in lista:
                if ele == alt:
                    #print(ele)
                    #Pedir os dados a serem alterados
                    new_name = input("Indique o novo login:")
                    new_passe = input("Indique a nova passe:")
                    index_ele = lista.index(ele)

                    #Alterar os valores na respetiva lista
                    rows[index_lista][index_ele+1] = new_name
                    rows[index_lista][index_ele+2] = new_passe
                    
                    #Mostrar que os dados foram alterados com sucesso
                    #print(rows)
                    print("Dados de acesso alterados com acesso!!!")
                    
                    #acabar o while
                    procurar = 0
               
        print("Dados não encontrados!!!")

        #Guardar a lista rows alterada no ficheiro csv
        with open ("passes.csv","w", encoding="UTF-8") as csv_file:
            write = csv.writer(csv_file)
            for lista in rows:
                write.writerow(lista)
            csv_file.close()
        
                    
def delPass():
    rows = []

    #Abrir o ficheiro das passes e passar para uma lista de listas
    with open ("passes.csv","r", encoding="UTF-8") as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
                rows.append(row)
    
    #Apagar as listas vazias dentro da lista de listas
    rows = [ele for ele in rows if ele != []]

    

    procurar = 1
    #fazer um ciclo para percorrer as listas
    while procurar == 1:
          #Perguntar ao utilizador qual a passe a remo1ver
        delet = input("Qual a palavra passe que pretende remover: ")
        for lista in rows:
            index_lista = rows.index(lista)
            for ele in lista:
                if ele == delet:

                    verify = input("Tem a certeza que pretende apagar? (S/N) ")
                    if verify == "S":
                        rows.remove(lista)
                        
                        #Mostrar que os dados foram alterados com sucesso
                        #print(rows)
                        print("Dados apagados com sucesso!!!")
                        
                        #acabar o while
                        procurar = 0
                        break
                    
        print("Dados não encontrados!!!")
                    
                    
    with open ("passes.csv","w", encoding="UTF-8") as csv_file:
            write = csv.writer(csv_file)
            for lista in rows:
                write.writerow(lista)
            csv_file.close()
                    
                 
def mostrarPass(site):
    rows = []
    #Abrir ficheiro e adicionar valores a uma lista de listas
    with open ("passes.csv","r", encoding="UTF-8") as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
                rows.append(row)

    #Apagar as listas vazias dentro da lista de listas
    rows = [ele for ele in rows if ele != []]


    #perguntar ao utilizador se pretende ver alguma palavra passe especifica
    

    for lista in rows:
        #index de cada lista
        index_lista = rows.index(lista)
        for ele in lista:
            if site == ele:
                 print(rows[index_lista])
                 csv_file.close()


def mostrarTodasPasses():
    rows = []
     #Abrir ficheiro e adicionar valores a uma lista de listas
    with open ("passes.csv","r", encoding="UTF-8") as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
                rows.append(row)

    rows = [ele for ele in rows if ele != []]
    
    #mostrar todas as listas existentes dentro da lista


    
    # for lista in rows:
    #     # print(lista[0] ,",",lista[1] ,",",lista[2])
    #     print(tabulate([lista],headers=col_names, tablefmt="fancy_grid"))
       
    data_header = rows[0]
    data_values = rows[1:]

    print(tabulate(data_values, headers=data_header,tablefmt="fancy_grid"))




def code():
    rows = []
    #Abrir ficheiro e adicionar valores a uma lista de listas
    with open ("passes.csv","r", encoding="UTF-8") as csv_file:
        csvreader = csv.reader(csv_file)
        for row in csvreader:
                rows.append(row)

    #Apagar as listas vazias dentro da lista de listas
    rows = [ele for ele in rows if ele != []]

    conversion_code = {   
    'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V', 'F': 'U', 
    'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q', 'K': 'P', 'L': 'O', 
    'M': 'N', 'N': 'M', 'O': 'L', 'P': 'K', 'Q': 'J', 'R': 'I', 
    'S': 'H', 'T': 'G', 'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 
    'Y': 'B', 'Z': 'A', 
  
    
    'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 
    'g': 't', 'h': 's', 'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o', 
    'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i', 
    's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 
    'y': 'b', 'z': 'a'
    } 
    
    

    for i, lista in enumerate(rows):
        #print (i, ",",lista)
        for j,val in enumerate(lista):
            #print(j,",",val)
            #create empty string
            converted_data = ""
            #print("--------------------------------")
            for letra in val:
                #print(letra,",")
                if letra in conversion_code.keys():
                    converted_data += conversion_code[letra]
                else:
                     converted_data += letra
                rows[i][j] = converted_data
   
    
    with open ("passes.csv","w", encoding="UTF-8") as csv_file:
            write = csv.writer(csv_file)
            for lista in rows:
                write.writerow(lista)
            csv_file.close()


     
def menu():

    
    menu = 1


    while menu == 1:
        print("---------------------------------------------")
        print("-                                           -")
        print("- 1 - Adicionar password                    -")
        print("- 2 - Mudar password                        -")
        print("- 3 - Apagar password                       -")
        print("- 4 - Mostar passwords                      -")
        print("- 5 - Sair                                  -")
        print("-                                           -")
        print("---------------------------------------------")

        resposta = int(input("Escolha uma opção do menu:"))
        
             
        

        
            
             

        if resposta == 1:
            site = input("Indique o site: ")
            login = input("Indique o login: ")
            senha = input("Indique a senha: ")
            addPass(site,login,senha)           
        if resposta == 2:
             changePass()
        if resposta == 3:
             delPass()
        if resposta == 4:
             mostrarTodasPasses()
             
             resposta_2 = input("Pretende procurar por algo especifico? (S / N) ")
             if resposta_2 == "S":
                
                mostrar= input("Qual a conta que pretende ver: ")
                mostrarPass(mostrar)
        if resposta == 5:
             code()
             print("Coding passwords...") 
             menu = 0
        else:
             print("Resposta inválida")
        
#Testes durante a realização
                
# addPass("insta","1","1")
# addPass("facebook","2","2")
# addPass("twitter","3","3")
#delPass()
#mostrarPass("facebook")
#changePass()
#codeDecode()
code()
print("Decoding passwords...") 
menu()