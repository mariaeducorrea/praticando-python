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