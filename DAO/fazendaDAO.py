from classBanco import Banco

banco = Banco()

def ver_fazenda():
    print("VER FAZENDA")

    fazendas = banco.consultar('''
            SELECT * FROM fazenda
''')

    if len(fazendas) == 0:
        print("Nenhuma fazenda enocntrada.")
        return

    print(f"{'CÓDIGO':<10} {'NOME':<20} {'DONO':<20} {'CIDADE':<20} {'CONTATO':<15}")

    for fazenda in fazendas:
        print(f"{fazenda[0]:<10} {fazenda[1]:<20} {fazenda[2]:<20} {fazenda[3]:<20} {fazenda[4]:<15}")


def cadastrar_fazenda():
    print("CADASTRAMENTO")

    nome = input("Digite o nome da fazenda: ")
    dono = input("Digite o nome do dono da fazenda: ")
    cidade = input("Digite a cidade da fazenda: ")
    contato = input("Digite o contato da fazenda: ")

    banco.manipular('''
            INSERT INTO fazenda
            VALUES(default, %s, %s, %s, %s)
''', (nome, dono, cidade, contato))

    print("FAZENDA CADASTRADA!")




    