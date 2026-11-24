from classBanco import Banco

banco = Banco()


def buscar_animal_id(id_animal):

    animal = banco.consultar('''
            SELECT * FROM animal
            WHERE cod_animal = %s

''', (id_animal,))

    if len(animal) > 0:
        return animal[0]
    else:
        return None



def ver_animal_disponivel():
    print("ANIMAIS DISPONÍVEIS")

    animal_disponivel = banco.consultar('''
            SELECT * FROM animal
            WHERE status = 'disponivel'
''')

    print(f"{'CÓDIGO':<8} {'RAÇA':<15} {'BRINCO':<10} {'SEXO':<10} {'TIPO':<12} {'COD FAZENDA':<12} {'STATUS':<15}")

    for a in animal_disponivel:
            print("-" * 30)
            print(f"CÓDIGO:       {a[0]}")
            print(f"RAÇA:         {a[1]}")
            print(f"BRINCO:       {a[2]}")
            print(f"SEXO:         {a[3]}")
            print(f"TIPO:         {a[4]}")
            print(f"CÓD FAZENDA:  {a[5]}")
            print(f"STATUS:       {a[6]}")
            print("-" * 30)

    

def ver_animal():
    print("VER ANIMAIS")

    animal = banco.consultar('''
            SELECT * FROM animal
''')

    if not animal:
        print("Animal não encontrado.")
        return

    print(f"{'CÓDIGO':<8} {'RAÇA':<15} {'BRINCO':<10} {'SEXO':<10} {'TIPO':<12} {'COD FAZENDA':<12} {'STATUS':<15}")

    for a in animal:
            print("-" * 30)
            print(f"CÓDIGO:       {a[0]}")
            print(f"RAÇA:         {a[1]}")
            print(f"BRINCO:       {a[2]}")
            print(f"SEXO:         {a[3]}")
            print(f"TIPO:         {a[4]}")
            print(f"CÓD FAZENDA:  {a[5]}")
            print(f"STATUS:       {a[6]}")
            print("-" * 30)



def cadastrar_animal():
    print("CADASTRO DE ANIMAL")

    raca = input("Digite a raça do animal: ")
    brinco = input("Digite o código do brinco do animal: ")
    sexo = input("Digite o sexo do animal (macho/fêmea): ")
    tipo = input("Digite o tipo da vaca (doadora/repeptora): ")
    cod_fazenda = int(input("Digite o código da fazenda do animal: "))
    status = input("Digite o status do animal para procedimentos (disponível/indisponível): " )

    banco.manipular('''
            INSERT INTO animal
            VALUES(default, %s, %s, %s, %s, %s, %s)
''', (raca, brinco, sexo, tipo, cod_fazenda, status,))





def alterar_animal():
    print("ALTERAÇÃO DO ANIMAL")

    ver_animal()

    cod_animal =int(input("Digite o animal que deseja alterar: "))

    animal = banco.consultar('''
            SELECT * FROM animal
            WHERE cod_animal = %s
''', (cod_animal,))

    print(f"""
        INFORMAÇÕES DO ANIMAL:
        Código: {animal[0]}
        Raça: {animal[1]}
        Brinco: {animal[2]}
        Sexo: {animal[3]}
        Tipo: {animal[4]}
        Código da Fazenda: {animal[5]}
        Status: {animal[6]}
""")

    continuar = input("Deseja continuar e alterar as informações desse animal (S/N): ")

    if continuar != "S":
        return

    raca_novo = input("Digite a nova raça do animal: ")

    if raca_novo:
        raca_novo = animal[1]
         
    novo_brinco = input("Digite o novo brinco do animal: ")

    if novo_brinco:
         novo_brinco = animal[2]

    novo_sexo = input("Digite a novo sexo do animal: ")

    if not novo_sexo:
        novo_sexo = animal[3]

    if animal[3] != novo_sexo:
        if novo_sexo == "Macho":
            banco.manipular('''
                UPDATE coleta
                SET tipo = 'Coleta de sêmen'
                WHERE cod_animal = %s
    ''', (cod_animal,))

        else:
            banco.manipular('''
                UPDATE coleta
                SET tipo = 'Aspiração folicular'
                WHERE cod_animal = %s
    ''', (cod_animal,))


    novo_tipo = input("Digite o tipo do animal (doadora/receptora): ")

    if not novo_tipo:
         novo_tipo = animal[4]

    novo_cod_fazenda = int(input("Digite o novo código da fazenda do animal: "))

    if not novo_cod_fazenda:
         novo_cod_fazenda = animal[5]

    novo_status = input("Digite o status do animal: ")

    if not novo_status:
        novo_status = animal[6]

    banco.manipular('''
            UPDATE animal
            SET raca = %s, brinco = %s, sexo = %s, tipo = %s, cod_fazenda = %s, status = %s
            WHERE = cod_animal = %s
''', (raca_novo, novo_brinco, novo_sexo, novo_tipo, novo_cod_fazenda, novo_status, cod_animal,))







    

    





    

    
