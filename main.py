from classBanco import Banco 
from datetime import datetime
from DAO import animalDAO, coletaDAO, fazendaDAO

banco = Banco()

while True:
    print("""
        BEM VINDO AO FORT EMBRYO.
        GERENCIE ANIMAIS E COLETAS DE FORMA SIMPLES E PRÁTICA.

        Opções:
            1. Ver animais.
            2. Cadastrar animal.
            3. Alterar cadastro do animal.
            4. Remover animal.
            5. Ver coletas.
            6. Cadastrar coletas.
            7. Ver fazendas.
            8.  Cadastro de fazenda.
            0. Sair.
""")

    opcao = input("Digite o número da opção desejada ")

    if opcao == "1":
        animalDAO.ver_animal()

    elif opcao == "2":
        animalDAO.cadastrar_animal()

    elif opcao == "3":
        pass

    elif opcao == "4":
        pass

    elif opcao == "5":
        coletaDAO.ver_coleta()

    elif opcao == "6":
        coletaDAO.cadastrar_coleta()

    elif opcao == "7":
        fazendaDAO.ver_fazenda()

    elif opcao == "8":
        fazendaDAO.cadastrar_fazenda()

    elif opcao == "0":
        print("Encerrando programa...")

    else:
        print("Digite uma opção válida.")

    input("TECLE ENTER PARA CONTINUAR")
