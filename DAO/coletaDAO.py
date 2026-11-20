from classBanco import Banco
from datetime import datetime
from DAO import animalDAO

banco = Banco()

def ver_coleta():
    print("VER CADASTRO")

    coleta = banco.consultar('''
            SELECT * FROM coleta
''')

    if not coleta:
        print("coleta não encontrada.")
        return


    print(f"{'CÓDIGO':<8} {'DATA':<12} {'TIPO':<25} {'COD ANIMAL':<12} {'COD LABORATÓRIO':<18} {'COD FUNCIONÁRIO':<18}")

    for c in coleta:
        print("-" * 35)
        print(f"CÓDIGO:          {c[0]}")
        print(f"DATA:            {c[1]}")
        print(f"TIPO:            {c[2]}")
        print(f"CÓD ANIMAL:      {c[3]}")
        print(f"CÓD LABORATÓRIO: {c[4]}")
        print(f"CÓD FUNCIONÁRIO: {c[5]}")
        print("-" * 35)




def cadastrar_coleta():
    print("CADASTRO DA COLETA")

    data = input("Digite a data da coleta (dd/mm/aaaa): ")
    
    if data:
        data_formatada = datetime.strptime(data, "%d/%m/%Y")
        data = data_formatada

    cod_animal = None
    tipo_coleta = None

    while True:
        animalDAO.ver_animal_disponivel()

        cod_animal = int(input("Digite o código do animal: "))

        animal = animalDAO.buscar_animal_id(cod_animal)

        if animal[6] == "indisponivel":
            print("Animal indisponível para coleta.")
            continue

        if animal[3] == "Macho":
            tipo_coleta = 'Coleta de sêmen'
        else:
            tipo_coleta = 'Aspiração folicular'
        break


    cod_laboratorio = int(input("Digite o código do laboratório: "))
    cod_funcionario = int(input("Digite o código do funcionário que fez a coleta: "))

    banco.manipular('''
            INSERT INTO coleta
            VALUES(default, %s, %s, %s, %s, %s)
''', (data_formatada, tipo_coleta, cod_animal, cod_laboratorio, cod_funcionario,))

    banco.manipular('''
            UPDATE animal
            SET status = 'indisponivel'
            WHERE cod_animal = %s
''', (cod_animal,))