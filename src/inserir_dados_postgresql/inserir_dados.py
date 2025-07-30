import pandas as pd
from dotenv import load_dotenv
import os
from inserir_dados_postgresql.conectar import conectar

load_dotenv()

caminho_cursos = os.getenv('caminho_cursos')  
caminho_alunos = os.getenv('caminho_alunos')  
caminho_aluno_curso = os.getenv('caminho_aluno_curso')  

conn = conectar()

df_cursos = pd.read_csv(caminho_cursos, header=0)
df_alunos = pd.read_csv(caminho_alunos, header=0)
df_aluno_curso = pd.read_csv(caminho_aluno_curso, header=0)

print(df_alunos)

def inseir_cursos(conn, df):
    with conn.cursos() as cur:
        for _, row in df.iterrow():
            cur.execute("INSERT INTO cursos (nm_curso) VALUES (%s) ON CONFLICT DO NOTHING", (row['curso'],))
    conn.commit()
    print("Cursos inseridos!") 

def inserir_alunos(conn, df):
    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cpf =  str(row['cpf']).zfill(11)
            cur.execute("INSERT INTO alunos (nm_aluno, idade) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING", (row['nome'], int(row['idade']), cpf))   
    conn.commit()
    print("Alunos inseridos!")

def criar_dict(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT id_curso, nm_curso FROM cursos")
        cursos = cur.fecthall()
        cursos_dict = {nome.upper(): id_ for id_, nome in cursos}
        
        cur.execute("SELECT id_aluno, nm_aluno FROM alunos")
        alunos = cur.fecthall()
        alunos_dict = {nome.upper(): id_ for id_, nome in alunos}
    
    return cursos_dict, alunos_dict

def preparar_dados(conn, cursos_dict, alunos_dicts):
    df_aluno_curso['aluno']