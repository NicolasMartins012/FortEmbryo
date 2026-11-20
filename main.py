from classBanco import Banco 
from datetime import datetime
from DAO import animalDAO, coletaDAO

banco = Banco()

while True:
    print("""
        BEM VINDO AO FORT EMBRYO.
        GERENCIE ANIMAIS E COLETAS DE FORMA SIMPLES E PRÁTICA.

        Opções de visualização:
            1. Ver animais.
            2. Cadastrar animal.
            3. Ver coletas.
            4. Cadastrar coletas.
            5. Ver fazendas.
            5. Cadastro de fazenda.
            0. Sair.
""")

    opcao = input("Digite o número da opção desejada ")

    if opcao == "1":
        animalDAO.ver_animal()

    elif opcao == "2":
        animalDAO.cadastrar_animal()

    elif opcao == "3":
        coletaDAO.ver_coleta()

    elif opcao == "4":
        coletaDAO.cadastrar_coleta()

    elif opcao == "5":
        pass

    elif opcao == "6":
        pass

    elif opcao == "0":
        print("Encerrando programa...")

    else:
        print("Digite uma opção válida.")

    input("TECLE ENTER PARA CONTINUAR")
