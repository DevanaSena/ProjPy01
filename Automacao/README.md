## Processo de Automação com Python 1 dia

Durante a Jornada Python da Hasttag no primeiro dia o Power UP, aprendi a desenvolver um projeto de automação utilizando a linguagem Python, focado em automatizar o cadastro de produtos em um sistema. As principais tecnologias e ferramentas que utilizei foram:

<strong>Biblioteca Pandas:</strong> Para importar e visualizar a base de dados (arquivo CSV) de produtos, facilitando a manipulação e análise das informações.<br><br>
<strong>Biblioteca PyAutoGUI:</strong> Para controlar o mouse e o teclado, permitindo a automação das ações necessárias para o cadastro dos produtos no sistema. Utilizei os comandos pyautogui.press (pressionar teclas), pyautogui.write (digitar texto) e pyautogui.click (clicar com o mouse).<br><br>
<strong>Estruturas de Repetição e Condicionais:</strong> Para percorrer a base de dados e realizar o cadastro automático de cada produto, verificando e preenchendo os campos necessários no sistema.<br><br>
<strong>Automação de Tarefas:</strong> Criei scripts para abrir o navegador, acessar o sistema, realizar login e cadastrar produtos, otimizando processos manuais e minimizando erros.<br><br>
Este projeto me proporcionou uma visão prática de como a automação pode ser aplicada para aumentar a produtividade e a eficiência no ambiente de trabalho.

![aula1PythonAutomacao](https://github.com/DevanaSena/ProjPy01/assets/145565646/efa4bc18-c087-4d13-8b86-8c5d9ec8aef7)


# Setup
  - Instalação do vscode criação da 📂 do projeto e um arquivo py.
	- Entrar no sistema da emoresa 
	- https://dlp.hashtagtreinamentos.com/python/intensivao/login
		- pip install pyautogui
		- python.exe -m pip install --upgrade pip

# Comandos do Pyautogui

	- Realizar o login
	- Importar a base de dados 
	- Cadastrar um produto
	- Repetir o processo até o cadastro acabar

# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

```python

import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.6
pyautogui.scroll(50)

# pip install pyautogui
# python.exe -m pip install --upgrade pip

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# Docmumentação https://pyautogui.readthedocs.io/en/latest/
#pyautogui.hotkey("ctrl", "v")

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=685, y=451)
# escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=955, y=638) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim 
´´´



