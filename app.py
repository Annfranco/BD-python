import os 
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
OUTRO_BANCO = create_engine("sqlite:///outrobanco.db")

# Criando conexão com banco de dados.
Session = sessionmaker(bind=OUTRO_BANCO)
session = Session()

# Criando tabela.
Base = declarative_base()

def consultar(Aluno):
    # R - Read - select - Consulta
    print("\nExibindo dados de todos os clientes.")
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

def atualizar(Aluno):
    # U - Update - UPDATE - Atualizar
    print("\nAtualizando dados dos alunos.")
    email_aluno = input("Digite o e-mail do aluno que será atualizado: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno: 
        aluno.nome = input("Digite seu nome: ")
        aluno.sobrenome = input("Digite seu sobrenome: ")
        aluno.email = input("Digite seu email: ")
        aluno.senha = input("Digite sua senha: ")

        session.commit()
    else:
        print("Aluno não encontrado.")

def excluir(Aluno):
    # D - Delete - DELETE - Excluir 
    print("\nExcluindo os dados de um aluno.")
    email_aluno = input("Digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Cliente {aluno.nome} excluido com sucesso!")
    else:
        print("Cliente não encontrado.")

def consultar_apenas_um(Aluno):
    # R - Read - select - Consulta
    print("Consultando os dados de apenas um aluno.")
    email_aluno = input("Digite o e-mail do aluno que deseja consultar: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")
    else:
        print("Cliente não encontrado.")

class Aluno(Base):
    __tablename__ = "Alunos"

    # Definindo campos da tabela.
    ra = Column("R.A.", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome:str, sobrenome:str, email:str, senha:str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha  

# Criando tabela no banco de dados.
Base.metadata.create_all(bind=OUTRO_BANCO)

# CRUD
# Create - Insert - Salvar.
os.system("cls || clear")
print("Solicitando dados para o aluno.")
inserir_nome = input("Digite seu nome: ")
inserir_sobrenome = input("Digite seu sobrenome: ")
inserir_email = input("Digite seu email: ")
inserir_senha = input("Digite sua senha: ")

aluno = Aluno(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
session.add(aluno)
session.commit()

while True: 
    print("\n1. Consultar Usuarios.")
    print("2. Deletar Usuario.")
    print("3. Atualizar Usuario.")
    print("4. Consultar 1 Usuario.")
    print("5. Sair")

    opcao = int(input("\nInforme a opção desejada: "))

    match(opcao):
        case 1:
            consulta = consultar(Aluno)
            resposta = input("\nDeseja escolher mais uma opção do menu? ")
            if resposta == "nao":
                break
        case 2:
            deletar = excluir(Aluno)
            resposta = input("\nDeseja escolher mais uma opção do menu? ")
            if resposta == "nao":
                break
        case 3:
            atualiza = atualizar(Aluno)
            resposta = input("\nDeseja escolher mais uma opção do menu? ")
            if resposta == "nao":
                break
        case 4:
            consultar_um = consultar_apenas_um(Aluno)
            resposta = input("\nDeseja escolher mais uma opção do menu? ")
            if resposta == "nao":
                break
        case 5:
            print("\nSair.")
            break
        case _:
            print("\nOpção Invalida. Tente Novamente.")

# Fechando conexão.
session.close()