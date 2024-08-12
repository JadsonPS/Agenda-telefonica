
# importa o sqlites
import sqlite3
# importando a tkinter
from tkinter import *
import os

# cria a conexão com o arquivo do banco de dados
banco_conexao = sqlite3.connect('Agenda.db')

# criar cursor para executar os comandos SQL para realizar no banco
cursor = banco_conexao.cursor()

#bloco pra verificar se uma tabela já existe ou não no computador, é só para rodar o código varias vezes, mas não 
try:
    #criar a tabela do banco de dados
    cursor.execute("""CREATE TABLE contatos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome text NOT NULL,
    fone VARCHAR(20))""")

    #inserir dados na tabela
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Regis', '1100000000');")
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Abigail', '1112345678');")
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Benedito', '1187654321');")
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Zacarias', '1199999999');")
except:
    
    #inserir dados na tabela
    """ cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Regis', '1100000000');")
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Abigail', '1112345678');")
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Benedito', '1187654321');")
    cursor.execute("INSERT INTO contatos (nome, fone) VALUES( 'Zacarias', '1199999999');") """
    pass




#confirmação dos dados no banco, você só usa esse comando se a ação edita algo no banco de dados
banco_conexao.commit()


# pegar os dados que estão no banco
cursor.execute('SELECT * FROM contatos')


# exibir os dados do banco
registros_cadastrados = cursor.fetchall()


# instrunções em python para mostrar os dados da tabela no terminal
titulo = f"|  {'ID'} | {'Nome':15}| {'Telefone':20}|"
comprimento_title = len(titulo)
#print("="*comprimento_title)
#print(titulo)
#print("="*comprimento_title)
"""totalDeContatos = len(registros_cadastrados)"""
totalDeContatos = 0
for pessoa in registros_cadastrados:
#    print(f"|{pessoa[0]:4} | {pessoa[1]:15}| {pessoa[2]:20}|")
    totalDeContatos += 1
#print("="*comprimento_title)


# Bloco de coódigo para cadastrar uma pessoa manualmente 
#cadastro=(input("PARA CADASTRAR UM NOVO CONTATO DIGITE [1]:\nPARA ENCERRAR A OPERAÇÃO DIGITE [0]\n"))

""" print ("Cadastrar um novo contato")
nome = input("Primeiro Nome: ")
fone = int(input("Telefone: "))
cursor.execute(f"INSERT INTO contatos (nome,fone) VALUES( '{nome}', '{fone}');")
banco_conexao.commit() """



#fecha a conexão
banco_conexao.close()
















#==============================================================================================================
"""                                Função de Consultar a lista de Clientes                                  """
#==============================================================================================================
def consulta():
      
    # cria a conexão com o arquivo do banco de dados
    banco_conexao = sqlite3.connect('Agenda.db')

    # criar cursor para executar os comandos SQL para realizar no banco
    cursor = banco_conexao.cursor()
    print("============================================")
    print("|             Consultar contato            |") 
    print("============================================")
    print("""| Opções de pesquisa:                      |
| [A] [B] [C] [D] [E] [F] [G] [H] [I] [J]  |
| [K] [L] [M] [N] [O] [P] [Q] [R] [S] [T]  |
| [U] [V] [X] [W] [Y] [Z] ["NOME CONTATO"] |
| [ Todos Contatos  ] [voltar]             |""")

    # pegar os dados que estão no banco
    #cursor.execute('SELECT * FROM contatos')
    # https://www.w3schools.com/sql/sql_like.asp ==================================================================================================================
    nome_pesquisado = str(input('| :> '))
    if (nome_pesquisado == "Todos Contatos") or (nome_pesquisado == "Todos contatos") or (nome_pesquisado == "todos contatos") or (nome_pesquisado == "Todo Contatos") or (nome_pesquisado == "Todos Contato") or (nome_pesquisado == "todo contato") or (nome_pesquisado == "Todo Contato") or (nome_pesquisado == "Todos os Contatos") or (nome_pesquisado == "Todos os contatos") or (nome_pesquisado == "todos os contatos"):
        cursor.execute("SELECT * FROM contatos")
    elif (nome_pesquisado == "voltar") or (nome_pesquisado == "Voltar") or (nome_pesquisado == "volta") or (nome_pesquisado == "Volta"):
        pass    
    else:
        cursor.execute(f"SELECT * FROM contatos WHERE nome LIKE '{nome_pesquisado}%'")

    # exibir os dados do banco
    registros_cadastrados = cursor.fetchall()

    # instrunções em python para mostrar os dados da tabela no terminal
    titulo = f"|  {"id"} | {"nome":15}| {"telefone":20}|"
    comprimento_title = len(titulo)
    print("="*comprimento_title)
    print(titulo)
    print("="*comprimento_title)
    for pessoa in registros_cadastrados:
        print(f"|{pessoa[0]:4} | {pessoa[1]:15}| {pessoa[2]:20}|")
    print("="*comprimento_title)

    #fecha a conexão
    banco_conexao.close()




#==============================================================================================================
"""                                    Função de Cadastrar novos Clientes                                   """
#==============================================================================================================
def cadastrar():
    # cria a conexão com o arquivo do banco de dados
    banco_conexao = sqlite3.connect('Agenda.db')

    # criar cursor para executar os comandos SQL para realizar no banco
    cursor = banco_conexao.cursor()

    # cadastrar novo cliente
    print("=================================")
    print("|   Cadastrar um novo contato   |") 
    print("=================================")
    repetir = True
    while repetir:
        nome = input("| Primeiro Nome: ")
        fone = int(input("| Telefone: "))
        confirmacao = False
        while not confirmacao:
            resposta_confirmando = input("""| Salvar   - [s]
| Editar   - [e]
| Cancelar - [c]
| :> """)
            print("")
            if resposta_confirmando == "s":
                cursor.execute(f"INSERT INTO contatos (nome,fone) VALUES( '{nome}', '{fone}');")
                banco_conexao.commit()

                #fecha a conexão com o banco de dados
                banco_conexao.close()
                
                print("*********************")
                print(" Novo contato salvo! ")
                print("*********************")
               
                #atualiza o total de contatos na agenda
                global totalDeContatos 
                totalDeContatos += 1
        
                confirmacao = True
                repetir = False
            elif resposta_confirmando == "e":
                print ("======================")
                print(f"| Nome: {nome}")
                print(f"| Telefône: {fone}")
                print("| Digite novamento os dados!")
                confirmacao = True
            elif resposta_confirmando == "c":
                print("********************")
                print(" Operação cancelada ")
                print("********************")
                confirmacao = True
                repetir = False
            else:
                print("*********************************")
                print(" Opção inválida tente novamente! ")
                print("*********************************")

#==============================================================================================================
"""                                Função de Edição e Exclusão de Clientes                                  """
#==============================================================================================================
def editar():
    repetir = True
    while repetir:
        print("=================================")
        print("|    Editar/Deletar contatos    |")
        print("=================================")
        print("| Editar contato         - [1]  |")
        print("| Excluir contato        - [2]  |")
        print("| Voltar                 - [3]  |")
        opcao = int(input("| :> "))
        print("")

        #==============================================================================================================
        """                                 Tela de opção de edição de Nome ou Telefone                             """
        #==============================================================================================================
        if opcao == 1:
            repetirEdicao = True
            while repetirEdicao:
                print("=================================")
                print("|         Editar contato        |")
                print("=================================")
                print("| Editar Nome            - [1]  |")
                print("| Editar Telefone        - [2]  |")
                print("| Voltar                 - [3]  |")
                opcaoEdicao = int(input("| :> "))
                print("")

                repetirPesquisaNomeContato = True
                while repetirPesquisaNomeContato:
                    #==============================================================================================================
                    """                                     Opção de edição do nome do contato                                  """
                    #==============================================================================================================
                    if opcaoEdicao == 1:
                        pesquisar_nome = input("| Qual o nome do contato que você quer alterar? ")

                        # cria a conexão com o arquivo do banco de dados
                        banco_conexao = sqlite3.connect('Agenda.db')
                        # criar cursor para executar os comandos SQL para realizar no banco
                        cursor = banco_conexao.cursor()

                        # pegar os dados que estão no banco
                        cursor.execute(f"SELECT * FROM contatos WHERE nome LIKE '{pesquisar_nome}%'")
                
                        # exibir os dados do banco
                        registros_cadastrados = cursor.fetchall()

                        # instrunções em python para mostrar os dados da tabela no terminal
                        titulo = f"|  {'ID'} | {'Nome':15}| {'Telefône':20}|"
                        comprimento_title = len(titulo)
                        print("="*comprimento_title)
                        print(titulo)
                        print("="*comprimento_title)
                        for pessoa in registros_cadastrados:
                            print(f"|{pessoa[0]:4} | {pessoa[1]:15}| {pessoa[2]:20}|")
                        print("="*comprimento_title)

                        opcaoEscolhaId = True
                        while opcaoEscolhaId:
                            print("| Digite o 'ID' do contato a ser editado, ")
                            print("| ou digite 'v' para VOLTAR a pesquisar novamente o nome do contato,")
                            print("| ou digite 'c' para CANCELAR! ")
                            idDoContatoParaEditar = input("| :> ")

                            # Se o valor digitado for um número será atualizado o nome do contato, mas se o valor for um 'v' ou um 'c' será feita operação de
                            # repetição ou cancelamento da atualização.
                            if idDoContatoParaEditar.isnumeric():
                                # pegar os dados que estão no banco
                                cursor.execute(f"SELECT * FROM contatos WHERE id={idDoContatoParaEditar}")
                        
                                # exibir os dados do banco
                                registros_cadastrados = cursor.fetchall()
                                
                                print(f"| Nome: {registros_cadastrados[0][1]} | Telefone: {registros_cadastrados[0][2]} |")
                                
                                novoNomeDoContatoParaEditar = input("| Editar nome: ")
                                print("| Salvar alteração - [s]")
                                print("| Cancelar operção - [qualquer letra]")
                                confirmacao = input("| :> ")
                                match confirmacao:
                                    case 's' | 'S' | 'sim' | 'Sim':
                                        cursor.execute(f"UPDATE contatos SET nome='{novoNomeDoContatoParaEditar}'WHERE id={int(idDoContatoParaEditar)};")
                                        banco_conexao.commit()
                                        #fecha a conexão com o banco de dados
                                        banco_conexao.close()
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case _:
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                            else:
                                match idDoContatoParaEditar:
                                    case 'v' | 'V':
                                        opcaoEscolhaId = False
                                        pass
                                    case 'c'| 'C':
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case _:
                                        print("*********************************")
                                        print(" Você digitou um valor inválido!")
                                        print("*********************************")    

                        
                    #==============================================================================================================
                    #"""                           Opção de edição do número do Telefone do contato                              """
                    #==============================================================================================================
                    elif opcaoEdicao == 2:
                        pesquisar_nome = input("| Qual o nome do contato que você quer alterar? ")

                        # cria a conexão com o arquivo do banco de dados
                        banco_conexao = sqlite3.connect('Agenda.db')
                        # criar cursor para executar os comandos SQL para realizar no banco
                        cursor = banco_conexao.cursor()

                        # pegar os dados que estão no banco
                        cursor.execute(f"SELECT * FROM contatos WHERE nome LIKE '{pesquisar_nome}%'")
                
                        # exibir os dados do banco
                        registros_cadastrados = cursor.fetchall()

                        # instrunções em python para mostrar os dados da tabela no terminal
                        titulo = f"|  {'ID'} | {'Nome':15}| {'Telefône':20}|"
                        comprimento_title = len(titulo)
                        print("="*comprimento_title)
                        print(titulo)
                        print("="*comprimento_title)
                        for pessoa in registros_cadastrados:
                            print(f"|{pessoa[0]:4} | {pessoa[1]:15}| {pessoa[2]:20}|")
                        print("="*comprimento_title)

                        opcaoEscolhaId = True
                        while opcaoEscolhaId:
                            print("| Digite o 'ID' do contato a ser editado, ")
                            print("| ou digite 'v' para VOLTAR a pesquisar novamente o nome do contato,")
                            print("| ou digite 'c' para CANCELAR! ")
                            idDoContatoParaEditar = input("| :> ")

                            # Se o valor digitado for um número será atualizado o nome do contato,
                            # mas se o valor for um 'v' ou um 'c' será feita operação de repetição
                            # ou cancelamento da atualização.
                            if idDoContatoParaEditar.isnumeric():
                                # pegar os dados que estão no banco
                                cursor.execute(f"SELECT * FROM contatos WHERE id={idDoContatoParaEditar}")
                        
                                # exibir os dados do banco
                                registros_cadastrados = cursor.fetchall()
                                
                                print(f"| Nome: {registros_cadastrados[0][1]} | Telefone: {registros_cadastrados[0][2]} |")
                                novoTelefoneDoContatoParaEditar = input("| Editar telefone: ")
                                print("| Salvar alteração - [s]")
                                print("| Cancelar operção - [qualquer letra]")
                                confirmacao = input("| :> ")
                                match confirmacao:
                                    case 's' | 'S' | 'sim' | 'Sim':
                                        cursor.execute(f"UPDATE contatos SET fone='{novoTelefoneDoContatoParaEditar}'WHERE id={int(idDoContatoParaEditar)};")
                                        banco_conexao.commit()
                                        #fecha a conexão com o banco de dados
                                        banco_conexao.close()
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case _:
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                            else:
                                match idDoContatoParaEditar:
                                    case 'v' | 'V':
                                        opcaoEscolhaId = False
                                        pass
                                    case 'c'| 'C':
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case _:
                                        print("*********************************")
                                        print(" Você digitou um valor inválido!")
                                        print("*********************************")    


                    #==============================================================================================================
                    #"""                                       Opção de Voltar tela anterior                                     """
                    #==============================================================================================================
                    # Voltar para tela anterior
                    elif opcaoEdicao == 3:
                        #comando para voltar a tela
                        repetirPesquisaNomeContato = False
                        repetirEdicao = False
                    else:
                        print(" Opção inválida tente novamente!")

              
        #==============================================================================================================
        #"""                                   Tela de opção de Exclusão de Contato                                  """
        #==============================================================================================================
        elif opcao == 2:
            repetirTelaExcluir = True
            while repetirTelaExcluir:
                print("=================================")
                print("|        Deletar contato        |")
                print("=================================")
                print("| Digite o nome do contato:     |")
                print('| Ou "voltar" |')
                opcaoDeletar = input("| :> ")
                print("")

                if (opcaoDeletar == "voltar") or (opcaoDeletar == "Voltar") or (opcaoDeletar == "volta") or (opcaoDeletar == "Volta") or (opcaoDeletar == "VOLTAR") or (opcaoDeletar == "VOLTAR"):
                    repetirTelaExcluir = False
                else:

                        # cria a conexão com o arquivo do banco de dados
                        banco_conexao = sqlite3.connect('Agenda.db')
                        # criar cursor para executar os comandos SQL para realizar no banco
                        cursor = banco_conexao.cursor()

                        # pegar os dados que estão no banco
                        cursor.execute(f"SELECT * FROM contatos WHERE nome LIKE '{opcaoDeletar}%'")
                
                        # exibir os dados do banco
                        registros_cadastrados = cursor.fetchall()

                        # instrunções em python para mostrar os dados da tabela no terminal
                        titulo = f"|  {'ID'} | {'Nome':15}| {'Telefône':20}|"
                        comprimento_title = len(titulo)
                        print("="*comprimento_title)
                        print(titulo)
                        print("="*comprimento_title)
                        for pessoa in registros_cadastrados:
                            print(f"|{pessoa[0]:4} | {pessoa[1]:15}| {pessoa[2]:20}|")
                        print("="*comprimento_title)

                        opcaoEscolhaId = True
                        while opcaoEscolhaId:
                            print("| Digite o 'ID' do contato ")
                            print("| ou digite 'v' para VOLTAR a pesquisar novamente o nome do contato,")
                            print("| ou digite 'c' para CANCELAR! ")
                            idDoContatoParaExcluir = input("| :> ")

                            # Se o valor digitado for um número será atualizado o nome do contato, mas se o valor for um 'v' ou um 'c' será feita operação de
                            # repetição ou cancelamento da atualização.
                            if idDoContatoParaExcluir.isnumeric():
                                # pegar os dados que estão no banco
                                cursor.execute(f"SELECT * FROM contatos WHERE id={idDoContatoParaExcluir}")
                        
                                # exibir os dados do banco
                                registros_cadastrados = cursor.fetchall()
                                
                                print(f"| Você deseja deletar o contato: |")
                                print(f"| Nome: {registros_cadastrados[0][1]}     |")
                                print(f"| Telefone: {registros_cadastrados[0][2]} |")
                                print("")
                                print("| Sim - [s]")
                                print("| Não - [n]")
                                confirmacao = input("| :> ")
                                match confirmacao:
                                    case 's' | 'S' | 'sim' | 'Sim':
                                       
                                        cursor.execute(f"DELETE FROM contatos WHERE id={int(idDoContatoParaExcluir)};")
                                        banco_conexao.commit()
                                        #fecha a conexão com o banco de dados
                                        banco_conexao.close()
                                        print("| Contato excluido com sucesso!")
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case 'n'|'N'|'não'|'Não':
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case _:
                                        print("*********************************")
                                        print(" Você digitou um valor inválido!")
                                        print("*********************************") 
                            else:
                                match idDoContatoParaExcluir:
                                    case 'v' | 'V':
                                        opcaoEscolhaId = False
                                        
                                    case 'c'| 'C':
                                        repetirPesquisaNomeContato = False
                                        opcaoEscolhaId = False
                                    case _:
                                        print("*********************************")
                                        print(" Você digitou um valor inválido!")
                                        print("*********************************")

        #==============================================================================================================
        #"""                                   Comando para voltar a tela anterior                                   """
        #==============================================================================================================
        elif opcao == 3:
            repetir = False
        else:
            print("*********************************")
            print(" Valor inválido tente novamente!")
            print("*********************************")


"""
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
============================================================================================================================================
"""

#==============================================================================================================
"""                                       Corpo principal do programa                                       """
#==============================================================================================================
while True:
    print("**************************************************************************")
    print("=================================")
    print("|              MENU             |")
    print("|       Agenda Telefônica       |")
    print("=================================")
    print(f"| Total de contatos: {totalDeContatos:10} |")
    print("| [1] - Consultar contatos      |")
    print("| [2] - Cadastrar novo contatos |")
    print("| [3] - Editar/Deletar contatos |")
    print("=================================")
    opcao = int(input("| :> "))
    print("")

    if opcao == 1:
        """Tela de consulta, onde busca os dados do banco de dados"""
        #print("Consultar dados")
        consulta()
        
    elif opcao == 2:
        """COMANDOS SQL DE CADASTRO de novos usuasior"""
        #print("Cadastrar usuário")
        cadastrar()
        
    elif opcao == 3:
        """Comandos de update"""
        #print("Atualizar usuário")
        editar()
        
    else:
        print(" Valor invalido")

