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