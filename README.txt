|==========================================================================|
|                                                                          |
|                                     |\|                                  |
|                                     |||                                  |
|                                     |||                                  |
|                                     |||                                  |
|                                     |||                                  |
|                                     |||                                  |
|                                     |||                                  |
|                                  ~-[{o}]-~                               |
|                                     |/|                                  |
|                                     |/|                                  |
|             ///~`     |\\_          `0'         =\\\\         . .        |
|            ,  |='  ,))\_| ~-_                    _)  \      _/_/|        |
|           / ,' ,;((((((    ~ \                  `~~~\-~-_ /~ (_/\        |
|        /' -~/~)))))))'\_   _/'                      \_  /'  D   |        |
|        (       (((((( ~-/ ~-/                          ~-;  /    \--_    |
|         ~~--|   ))''    ')  `                            `~~\_    \   )  |
|             :        (_  ~\           ,                    /~~-     ./   |
|              \        \_   )--__  /(_/)                   |    )    )|   |
|    ___       |_     \__/~-__    ~~   ,'      /,_;,   __--(   _/      |   |
|  //~~\`\    /' ~~~----|     ~~~~~~~~'        \-  ((~~    __-~        |   |
|((()   `\`\_(_     _-~~-\                      ``~~ ~~~~~~   \_      /    |
| )))     ~----'   /      \                                   )       )    |
|  (         ;`~--'        :                                _-    ,;;(     |
|            |    `\       |                             _-~    ,;;;;)     |
|            |    /'`\     ;                          _-~          _/      |
|           /~   /    |    )                         /;;;''  ,;;:-~        |
|          |    /     / | /                         |;;'   ,''             |
|          /   /     |  \\|                         |   ,;(                |
|        _/  /'       \  \_)                   .---__\_    \,--._______    |
|       ( )|'         (~-_|                   (;;'  ;;;~~~/' `;;|  `;;;\   |
|        ) `\_         |-_;;--__               ~~~----__/'    /'_______/   |
|        `----'       (   `~--_ ~~~;;------------~~~~~ ;;;'_/'             |
|                     `~~~~~~~~'~~~-----....___;;;____---~~                |
|                                                                          |
|==========================================================================|

                         Sistemas Operativos
                              2020/2021
                        
                              Grupo: 09
                        Cláudia Palmeiro - 50429
                        Luís Gonçalves - 46834
                        João Farrajota - 47141


|==========================================================================|
|                               Info                                       |
|==========================================================================|

Os ficheiros pgrepwc.py e pgrepwc_threads.py foram criados para fazer
a contagem do numero de ocurrencias de uma dada palavra ou o numero de
linhas onde essas ocorrencias ocorrem, em um ou mais ficheiros.

O ficheiro  pgrepwc.py faz essa contagem através de processos e o
ficheiro pgrepwc_threads.py faz essa contagem, atraves de threads.

Este programa só conta palavras que sejam directamente iguais ou que tenham 
associado um caracter especial à frente. No entanto este programa não
conta uma palavra com os mesmos caracteres, mas que tenha maiusculas/minusculas
diferentes da palavra de procura.

|==========================================================================|
|                              Comandos                                    |
|==========================================================================|

Para usar os programas basta inserir na consola os seguinte comandos:

    Para o caso de querermos usar multiplos processos/Threads:

        python3 A B -p C Nome Lista de ficheiros
    
        A: representa o ficheiro que pode ser pgrepwc.py (para usar processos)
        ou pgrepwc_threads.py (para usar Threads).
        
        B: São as opcoes de procura, que podem ser -c ou -l:
            
            -c :Serve para contar todas as ocorrencias de uma dada palavra em
                   um ou mais ficheiros.
    
            -l :Serve para contar o numero de linhas onde uma dada palavra 
                   ocorre em um ou mais ficheiros.
    
        C: representa o número de processos ou threads que queremos correr.
        Este numero tem de ser maior que 0 sempre que seguido pelo -p.
        
        Nome: É a palavra que queremos que o programa procure.
        
        lista de ficheiros: São os nomes dos ficheiros, onde queremos que o
        programa corre. Tem de ter nome válidos, onde cada ficheiro é separado
        por um espaco, como por exemplo:
        
        file1.txt
        exemplo1.txt exemplo2.txt
        teste1.txt teste2.txt teste3.txt
    
        Caso não seja dado uma lista de ficheiros, o programa pede na consola
        como input os nomes dos ficheiros

    Para o caso de não querermos usar multiplos processos/Threads:

        python3 A B Nome Lista de ficheiros
        
        A: representa o ficheiro que pode ser pgrepwc.py (para usar processos)
        ou pgrepwc_threads.py (para usar Threads).

        B: São as opcoes de procura, que podem ser -c ou -l:
            
            -c :Serve para contar todas as ocorrencias de uma dada palavra em
                   um ou mais ficheiros.
    
            -l :Serve para contar o numero de linhas onde uma dada palavra 
                   ocorre em um ou mais ficheiros.

        Nome: É a palavra que queremos que o programa procure.

        lista de ficheiros: São os nomes dos ficheiros, onde queremos que o
        programa corre. Tem de ter nome válidos, onde cada ficheiro é separado
        por um espaco, como por exemplo:
        
        file1.txt
        exemplo1.txt exemplo2.txt
        teste1.txt teste2.txt teste3.txt
    
        Caso não seja dado uma lista de ficheiros, o programa pede na consola
        como input os nomes dos ficheiros

|==========================================================================|
|                             Limitacoes                                   |
|==========================================================================|

    Todos os requisitos pedidos neste trabalho foram cumpridos.
    