from classBanco import Banco 
import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

banco = Banco()

conexaoDB = None
cursor = None

try:
    # 1. Criação e configuração da conexão e do cursor
    conexaoDB = psycopg.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode=os.getenv("DB_SSL")
    )

    cursor = conexaoDB.cursor()

    # DROP TABLES: 

    cursor.execute('DROP TABLE IF EXISTS coleta;')
    cursor.execute('DROP TABLE IF EXISTS animal;')
    cursor.execute('DROP TABLE IF EXISTS funcionario;')
    cursor.execute('DROP TABLE IF EXISTS laboratorio;')
    cursor.execute('DROP TABLE  IF EXISTS fazenda;')

    # CRIAÇÃO DAS TABELAS:

    cursor.execute('''
            CREATE TABLE fazenda(
            cod_fazenda INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_fazenda VARCHAR(245) NOT NULL,
            dono VARCHAR(245) NOT NULL,
            cidade VARCHAR(245),
            contato CHARACTER(11)
            )
''')

    cursor.execute('''
            CREATE TABLE laboratorio(
            cod_laboratorio INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_laboratorio VARCHAR(245) NOT NULL,
            cnpj CHARACTER(14) NOT NULL,
            endereco VARCHAR(245)
            )
''')

    cursor.execute('''
            CREATE TABLE funcionario(
            cod_funcionario INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            nome_funcionairo VARCHAR(245) NOT NULL,
            cpf CHARACTER(11) NOT NULL UNIQUE,
            cargo VARCHAR(245) NOT NULL,
            contato CHARACTER(11)
            )
''')

    cursor.execute('''
            CREATE TABLE animal(
            cod_animal INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            raca VARCHAR(245) NOT NULL DEFAULT 'Sem raça definida',
            brinco CHARACTER(50) NOT NULL, 
            sexo VARCHAR(245) NOT NULL,
            tipo VARCHAR(100) NOT NULL,
            cod_fazenda INTEGER NOT NULL,
            status VARCHAR(100) NOT NULL DEFAULT 'disponivel',

            CONSTRAINT ck_tipo CHECK (tipo in ('doadora', 'receptora')),
            CONSTRAINT fk_cod_fazenda FOREIGN KEY (cod_fazenda) REFERENCES fazenda (cod_fazenda),
            CONSTRAINT ck_status CHECK (status in ('disponivel', 'indisponivel'))
            )
''')

    cursor.execute('''
            CREATE TABLE coleta(
            cod_coleta INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            data DATE NOT NULL DEFAULT CURRENT_DATE,
            tipo_coleta VARCHAR(245) NOT NULL,
            cod_animal INTEGER NOT NULL,
            cod_laboratorio INTEGER NOT NULL,
            cod_funcionario INTEGER NOT NULL,

            CONSTRAINT fk_cod_animal FOREIGN KEY (cod_animal) REFERENCES animal (cod_animal),
            CONSTRAINT fk_cod_laboratoio FOREIGN KEY (cod_laboratorio) REFERENCES laboratorio (cod_laboratorio),
            CONSTRAINT fk_cod_funcionario FOREIGN KEY (cod_funcionario) REFERENCES funcionario (cod_funcionario)
            )
''')


    cursor.execute('''
        INSERT INTO fazenda
        (nome_fazenda, dono, cidade, contato)
        VALUES
        ('Fazenda Boa Esperança', 'Roberto Almeida', 'Quixeramobim', '88991234567'),
        ('Fazenda Santa Helena', 'Marcos Ferreira', 'Quixadá', '88987654321'),
        ('Fazenda Vale Verde', 'Antônio Carvalho', 'Morada Nova', '88993456789')
    ''')

    cursor.execute('''
        INSERT INTO laboratorio
        (nome_laboratorio, cnpj, endereco)
        VALUES
        ('Laboratório GenBio', '12345678000190', 'Fortaleza - CE'),
        ('Laboratório EmbryoTech', '23456789000191', 'Maracanaú - CE')
    ''')


    cursor.execute('''
        INSERT INTO animal
        (raca, brinco, sexo, tipo, cod_fazenda, status)
        VALUES
        ('Nelore', 'BR001', 'Fêmea', 'doadora', 1, 'disponivel'),
        ('Gir', 'BR002', 'Fêmea', 'receptora', 1, 'disponivel'),
        ('Holandesa', 'BR003', 'Fêmea', 'doadora', 2, 'disponivel'),
        ('Girolando', 'BR004', 'Fêmea', 'receptora', 2, 'disponivel'),
        ('Nelore', 'BR005', 'Fêmea', 'doadora', 3, 'disponivel'),
        ('Angus', 'BR006', 'Fêmea', 'receptora', 3, 'disponivel'),
        ('Nelore', 'BR007', 'Macho', 'doadora', 1, 'disponivel'),
        ('Angus', 'BR008', 'Macho', 'doadora', 2, 'disponivel'),
        ('Gir', 'BR009', 'Macho', 'doadora', 3, 'disponivel')
    ''')

    cursor.execute('''
        INSERT INTO funcionario
        (nome_funcionairo, cpf, cargo, contato)
        VALUES
        ('Lucas Martins', '12345678901', 'Técnico em Reprodução Animal', '85991234567'),
        ('Fernanda Oliveira', '23456789012', 'Veterinária', '85992345678'),
        ('Gabriel Souza', '34567890123', 'Analista de Laboratório', '85993456789')
    ''')


    cursor.execute('''
        INSERT INTO coleta
        (data, tipo_coleta, cod_animal, cod_laboratorio, cod_funcionario)
        VALUES
        ('2026-01-15', 'Aspiração folicular', 1, 1, 1),
        ('2026-01-18', 'Aspiração folicular', 3, 2, 2),
        ('2026-02-03', 'Aspiração folicular', 5, 1, 1),
        ('2026-02-10', 'Coleta de sêmen', 7, 2, 2),
        ('2026-02-17', 'Coleta de sêmen', 8, 1, 3),
        ('2026-03-05', 'Coleta de sêmen', 9, 2, 3)
    ''')


    conexaoDB.commit()

    print("TABELAS INSERIDAS!")
    print("INSERÇÕES FEITAS COM SUCESSO!")


except Exception as error:
    print("ERRO ENCONTRADO!", error)
    if conexaoDB is not None:
        conexaoDB.rollback()

finally:
    if cursor is not None:
        cursor.close()

    if conexaoDB is not None:
        conexaoDB.close()
