import pymysql.cursors
import time
import datetime

# Conexão do banco de dados com python
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='1337',
                             database='biblioteca',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

with connection: # Comando para Conexão
    with connection.cursor() as cursor:
        comandoselect = f'SELECT * FROM Produtos' # Comado do Select para Mostrar os campos
        cursor.execute(comandoselect) # Executar comando pedido
        resultado = cursor.fetchall() # Ler o banco de dados

        print(f'\033[1;33;40m-' *34,'TABELA PRODUTOS', '-' *35)
        for i in range(len(resultado)):# FOR para arrumar a lista dos campos
            print(f'Código do produto: {resultado[i]["CodigoDoProduto"]} | Nome do produto: {resultado[i]["NomeDoProduto"]} | Quantidade em estoque: {resultado[i]["QuantidadeEmEstoque"]} | Data do Cadastro: {resultado[i]["DataDoCadastro"]}')
        print(f'-'* 86, '\033[m')

        CodigoDoProduto = 0
        while CodigoDoProduto <= 0: # Laço de repetição para receber o código do produto
            CodigoDoProduto = int(input('\033[0;36;40mDigite o Código do Produto desejado: \033[m'))
        print('\033[0;36;40m-'* 86) 

        agora = datetime.datetime.now() # Pegar a data atual

        opc = 0 # Menu de Opções
        while opc != 4: # O programa ira rodar até a opção ser 4
            print('\033[0;36;40m1 - Nome do Produto \n2 - Quantidade em Estoque\n3 - Nome do Produto e Quantidade em Estoque\n4 - Sair')
            opc = int(input('Escolha uma opção: \033[m'))
            if opc == 1: # Opção 1
                print('\033[0;36;40m-'* 86)
                NomeDoProduto = input('Nome do Produto: \033[m')
                comando = f'UPDATE produtos SET NomeDoProduto = "{NomeDoProduto}", DataDoCadastro = "{agora}" WHERE CodigoDoProduto = "{CodigoDoProduto}"'
                break
            elif opc == 2: # Opção 2
                print('\033[0;36;40m-'* 86)
                QuantidadeEmEstoque = input('Quantidade em Estoque: \033[m')
                comando = f'UPDATE produtos SET QuantidadeEmEstoque = "{QuantidadeEmEstoque}", DataDoCadastro = "{agora}" WHERE CodigoDoProduto = "{CodigoDoProduto}"'
                break
            elif opc == 3: # Opção 3
                print('\033[0;36;40m-'* 86)
                NomeDoProduto = input('Nome do Produto: \033[m')
                QuantidadeEmEstoque = input('\033[0;36;40mQuantidade em Estoque: \033[m')
                comando = f'UPDATE produtos SET NomeDoProduto = "{NomeDoProduto}", QuantidadeEmEstoque = "{QuantidadeEmEstoque}", DataDoCadastro = "{agora}" WHERE CodigoDoProduto = "{CodigoDoProduto}"'
                break
            elif opc == 4: # Caso a opção for igual a 4, finalize o programa
                comando = f'UPDATE produtos SET NomeDoProduto = "", QuantidadeEmEstoque = "", DataDoCadastro = "" WHERE CodigoDoProduto = "-1"'
            else: # Se for digitado algum número errado nas opções
                print('\033[0;31;40m-'*86)
                print('\033[1;31;40mOpção Invalida!')
                print('\033[0;31;40m-'*86)
        print('\033[0;36;40m-'*86)
        print('\033[1;32;40mFinalizando', end='') # Finalização do programa
        time.sleep(1)

        for i in range(3): # For para os pontos
            print('.', end='')
            time.sleep(1)

        cursor.execute(comando) #Executa o comando
        connection.commit() #Faz um commit do comando executado

        print('')
        print('\033[1;32;40mComando Executado Com Sucesso')
        agora_string = agora.strftime("%d/%m/%Y %H:%M:%S") # Formatando a Data e hora
        print(agora_string)
