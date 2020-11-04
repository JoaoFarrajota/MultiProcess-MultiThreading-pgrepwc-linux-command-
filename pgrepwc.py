
from multiprocessing import Process, Value
import sys, os
import time


# -c -> opção que permite obter o numeroo de ocorrências encontradas da palavra a pesquisar
# -l -> opção que permite obter o numero de linhas devolvidas da pesquisa
# -n -> opção optcional permite definir por n o nível  de paralelizacao do comando 
# (ou seja o numero de processos filhos/threads que é usado para as pesquisas e contagem.
# caso seja omitido apenas um processo (o processo pai) é utilizado para fazer essas contagens e pesquisas

##### como correr na linha de comando ####
#$ python3 pgrepwc -c -p 2 joao f1 f2 f3
#$ python pgrepwc -c -p 2 joao f1 f2 f3
#$ python pgrepwc -c joao f1 f2

#sys.argv[0] ==> pgrepwc
#sys.argv[1] ==> -c ou -l
#sys.argv[2] ==> -p ou nome de procura
#sys.argv[3] ==> if sys.argv[2] == -p, então sys.argv[3] têm de ter um int. Se sys.argv[2] != -p então sys.argv[3:] têm de corresponder aos ficheiros
#sys.argv[4] ==> if sys.argv[2] == -p, então sys.argv[4] é o nome de procura
#sys.argv[5:] ==> têm de corresponder aos ficheiros


# Caracteres ess: 1 2 3 4 5 6 7 8 9 0 ? » « > < , ; : . ' " # $ % & / ( ) ! @ £ § { } = - _ * | \ + [ ] ª º ~ ^ 語  其

#string.isnumeric() - boolean   
#string.isalpha() - boolean



contador = Value("i", 0)

def pgrepwc(lista_argumentos):
    """
    This function will open a file or several files and read its contents, depending on the parameters the user inputed, it will return either the amount of chosen words or the amount of Lines that exists in all files, while using or not multi-processing.
    Requires: a list of arguments given by user with the command line 
    Ensures: the correct operation
    """
    # Verifica se o primeiro argumento é -c | -l Caso não seja lanca exceção
    if lista_argumentos[1] == "-c" or lista_argumentos[1] == "-l":
        
        # Obter o numero de ocorrencias da palavra
        if lista_argumentos[1] == '-c':

            # N. de filhos criados (paralelismo)
            if lista_argumentos[2] == '-p':
                        
                # Ficheiros a ser lidos
                if len(lista_argumentos[5:]) > 0:
                
                    option = lista_argumentos[1] # opção selecionada (-c or -l)
                    n = int(lista_argumentos[3]) # n. de filhos
                    name = lista_argumentos[4] # string que se procura
                    filesList = lista_argumentos[5:] # ficheiros

                    # numero de ficheiros < que processos // exemplo: 2 ficheiros para 4 processos
                    if len(filesList) < n:
                
                        n = len(filesList)
                        filesList = listaOrg(filesList, n)
                        criarFilhos(n, filesList, option, name)

                    # numero de ficheiros > ao numero de filhos criados // exemplo: 3 ficheiro para 1 processos 
                    elif len(filesList) > n:
        
                        filesList = listaOrg(filesList, n)
                        criarFilhos(n, filesList, option, name)
    
                    # numero de ficheiros igual ao numero de filhos criado    
                    elif len(filesList) == n:
                        
                        filesList = listaOrg(filesList, n)
                        criarFilhos(n, filesList, option, name)
            
                # sem ficheiros introduzidos e com o -p ativo
                else:
                    
                    filesList = input("Please input the name of your desired files: ")

                    option = lista_argumentos[1] # opção selecionada (-c or -l)
                    n = int(lista_argumentos[3]) # n. de filhos
                    name = lista_argumentos[4]  # string que se procura

                    filesList = listaOrg(filesList, n)
                    criarFilhos(n, filesList, option, name)
                
            # sem o -p n (o pai faz tudo) 
            else:
                # com ficheiros introduzidos no argv
                if len(lista_argumentos[3:]) > 0:
                    
                    name = lista_argumentos[2]
                    filesList = lista_argumentos[3:]
                    contarPalavras(name, filesList)

                # sem ficheiro
                else:
                    filesList = input("Please input the name of your desired files: ")

                    filesList = filesList.split(" ")
                    name = lista_argumentos[2]
                    contarPalavras(name, filesList)
                

            
        # Obter o numero de linhas         
        if lista_argumentos[1] == '-l':

            # N. de filhos criados (paralelismo)
            if lista_argumentos[2] == '-p':

                # Ficheiros a ser lidos
                if len(lista_argumentos[5:]) > 0:
                
                    option = lista_argumentos[1] # opção selecionada (-c or -l)
                    n = int(lista_argumentos[3]) # n. de filhos
                    name = lista_argumentos[4] # string que se procura
                    filesList = lista_argumentos[5:] # ficheiros

                    # Com processos
                    if len(filesList) < n:
                        n = len(filesList)
                        filesList = listaOrg(filesList, n)
                        criarFilhos(n, filesList, option, name)

                    # numero de ficheiros superior ao numero de filhos criados // exemplo: 3 ficheiro para 1 processos 
                    elif len(filesList) > n:
                        filesList = listaOrg(filesList, n)
                        criarFilhos(n, filesList, option, name)
    
                    # numero de ficheiros igual ao numero de filhos criado    
                    elif len(filesList) == n:
                        filesList = listaOrg(filesList, n)
                        criarFilhos(n, filesList, option, name)
            
                #sem ficheiros introduzidos
                else:
                    filesList = input("Please input the name of your desired files: ")

                    option = lista_argumentos[1] # opção selecionada (-c or -l)
                    n = int(lista_argumentos[3]) # n. de filhos
                    name = lista_argumentos[4]  # string que se procura

                    filesList = listaOrg(filesList, n)
                    criarFilhos(n, filesList, option, name)
        
            # sem o -p n (o pai faz tudo) 
            else:
                # com ficheiros introduzidos no argv
                if len(lista_argumentos[3:]) > 0:
                    
                    name = lista_argumentos[2]
                    filesList = lista_argumentos[3:]
                    contarLinhas(name, filesList)

                # sem ficheiro
                else:
                    filesList = input("Please input the name of your desired files: ")

                    filesList = filesList.split(" ")
                    name = lista_argumentos[2]
                    contarLinhas(name, filesList)

    else:
        raise Exception("First Argument must be either -c or -l")
    
            

def contarPalavras(name, fileList):
    """
    Counts the amount of chosen words that occur in a certain file.
    Requires: filename to be a valid file name in String and name to be a string.
    Ensures: The amount of times the words is present in the file as an Int. 
    """

    global pidPai
    
    for i in range(len(fileList)):
        counter = 0
        file = open(fileList[i], "r")

        if os.getpid()!=os.getppid():
            print("\n== Processo filho:" + str(os.getpid()) + " ==" + "\n" +"== Ficheiro " + fileList[i] + " ==\n")
        else:
            print("\n== Processo pai:" + str(os.getpid()) + " ==" + "\n" +"== Ficheiro " + fileList[i] + " ==\n")
  

        for line in file:
            
            list1 = line.split(" ")
            
            for j in list1:
                if name != j:
                    
                    if len(j) == len(name)+1 and name[:-1] == j[:-2]:
                        
                        if j[:-1].isnumeric() == False or j[:-1].isalpha() == False:
                            
                            counter+=1
                            print("linha encontrada: " + line + "\n")

                else:
                    counter+=1
                    print("linha encontrada: " + line + "\n")
                            
        print("Para a palavra " + name + " foram encontradas " + str(counter) + " ocorrencias\n")
        contador.value += counter                  
        file.close

    #print("Para a palavra " + name + " foram encontradas " + str(contador.value) + " instancias")

      

def contarLinhas(name, fileList):
    """
    Counts the amount of lines, where a chosen word exist, in a certain file
    Requires: filename to be a valid file name in string and name to be a string.
    Ensures: The amount of times the line where the chosen word exist is present in the file as an Int. 
    """
    global pidPai
 
    for i in range(len(fileList)):
        counter = 0
        file = open(fileList[i], "r")

        if os.getpid()!=pidPai:
            print("\n== Processo filho :" + str(os.getpid()) + " ==" + "\n" +"== Ficheiro " + fileList[i] + " ==\n")
        else:
            print("\n== Processo pai :" + str(os.getpid()) + " ==" + "\n" +"== Ficheiro " + fileList[i] + " ==\n")
        

        for line in file:
            #Coloca numa lista todos os elementos que estejam separados por um espaço(antes ou depois)
            list1 = line.split(" ")
        
            flag = False
            for j in list1:
                
                if name != j:
                    
                    if len(j)==len(name)+1 and name[:-1]==j[:-2]:
                       
                        if j[:-1].isnumeric() == False or j[:-1].isalpha() == False:
                            flag = True

 
                else:
                    flag = True


                    
            if flag == True:
                counter += 1
                print("linha encontrada: " + line + "\n")
                

        print("A palavra " + name + " foi encontrada em " + str(counter) + " linhas\n")
        contador.value += counter
        file.close
        
    
  
       
def listaOrg(listaFich, n):
    """
    divides and organizes a list of files according to n process
    Requires: ListaFich must be a one dimension list of String representing a filename.txt n must be an integer, representing a number of proceses.
    Ensures: A list of lists of String representing a filename.txt files that is well distribuited according
    """

    # Lista final onde onde vai estar os ficheiros organizados conforme o numero n (processos filhos)
    listaAns = []
   
    # variaveis auxiliares
    divInt = len(listaFich) // n #Se divInt= 2  significa que a cada dois elementos deposita numa lista
    rest = len(listaFich) % n
    

    if rest == 0:
        i = 0
        while i < n:
            listaTemp = []
            
            for j in range((divInt* (i + 1)) - divInt, (divInt* (i + 1))):
                listaTemp.append(listaFich[j])
            
            i = i + 1
            listaAns.append(listaTemp)
    else:
             
        i = 0
        while i < n:
            listaTemp = []
            
            for j in range((divInt* (i + 1)) - divInt, (divInt* (i + 1))):
                listaTemp.append(listaFich[j])
            
            i = i + 1
            listaAns.append(listaTemp)
        
        #lista dos ficheiros que falta distribuir       
        listaRest = []
       
        for j in range(divInt*n, len(listaFich)):
            listaRest.append(listaFich[j])

        #Distribui os elementos da listaRest pelos elementos da listaAns.
        for h in range(len(listaRest)):
            listaAns[h].append(listaRest[h])

    return listaAns



def criarFilhos(n, filesList, option, name):
    """
    Creates 'n' amount of child processes 
    Requires: 'n' to be and Int, filesList must be a list of String representing the name of files, option must be either a String of -c or -l, name must be a String. len(filesList) == n.
    Ensures: 'n' child processes. 
    [[1] , [2]] [[1]]
    """
    
    
    processList=[]
    if option == "-c":
     
        for i in range(len(filesList)):
            processList.append(Process(target = contarPalavras, args=(name, filesList[i])))
                   

    elif option == "-l":
        
        for i in range(len(filesList)):
            processList.append(Process(target = contarLinhas, args=(name, filesList[i])))
              

    for i in range(len(processList)):
        processList[i].start()
        time.sleep(1)
                    
    for i in range(len(processList)):
        processList[i].join()
    
 
    
lista_argumentos = sys.argv
pidPai = os.getpid()
pgrepwc(lista_argumentos)
print("== Pai " + (str(os.getpid()) + " ==\nO total de ocorrencias = " + str(contador.value)))

