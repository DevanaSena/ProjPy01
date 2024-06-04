import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.6
pyautogui.scroll(150)

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
time.sleep(3)

# entrar no linkannapaulassenna@gmail.com   1234    
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# pausa 
time.sleep(3)

pyautogui.click(x=1932, y=398) #clikes=2 | buttom="left|rigth|middle"

pyautogui.write("annapaulassenna@gmail.com")

pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.press("tab")
pyautogui.press("enter")

# Passo 3: Importar a base de produtos pra cadastrar
# pip install pandas numpy openpyxl

#import pandas 
#import pandas as pd

tabela = pandas.read_csv("produtos.csv")
# ler a base de dados
time.sleep(3)

print(tabela)
#         codigo       marca        tipo  categoria  preco_unitario  custo               obs
# 0    MOLO000251    Logitech       Mouse          1           25.95    6.5               NaN
# 1    MOLO000192    Logitech       Mouse          2           19.95    5.0               NaN
# 2    CAHA000251     Hashtag      Camisa          1           25.00   11.0               NaN
# 3    CAHA000252     Hashtag      Camisa          2           25.00   11.0  Conferir estoque
# 4    MOMU000111  Multilaser       Mouse          1           11.99    3.4               NaN
# ..          ...         ...         ...        ...             ...    ...               ...
# 288  ACAP000192       Apple  Acessorios          2           19.00    3.8               NaN
# 289  ACSA0009.3     Samsung  Acessorios          3            9.55    2.1               NaN
# 290  CEMO000271    Motorola     Celular          1          279.00   72.5               NaN
# 291  FOMO000152    Motorola        Fone          2          150.00   33.0               NaN
# 292  CEMO000223    Motorola     Celular          3          229.00   55.0               NaN
time.sleep(3)

 # Passo 4: Cadastrar um produto
 # para cada linha da tabela # for coluna in tabela.columns:

for linha in tabela.index:

    pyautogui.click(x=1863, y=285)

    #codigo = tabela.loc(4,"codigo")
    #pyautogui.press("Código do Produto")
    #pyautogui.write("1234")
    #pyautogui.press("tab")
    
    # Codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # Marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    # se observação de obs nao tiver vazia 
    if not pandas.isna(obs): 
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    # Passo 5: Repetir o processo de cadastro até o fim
    pyautogui.scroll(5000)