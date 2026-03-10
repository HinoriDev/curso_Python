# Bibliotecas = pacotes de códigos
import pyautogui # pyautogui (pacote de código para automação de tarefas) / # pip install pyautogui (instalação do pacote de código)
import time # biblioteca para trabalhar com tempo (pausas, etc)
#pyautogui.click -> clicar
#pyautogui.write -> escrever um texto
#pyautogui.press -> aperta uma tecla
#pyautogui.hotkey -> aperta um atalho
pyautogui.PAUSE = 0.5 # tempo de espera entre cada comando (0.5 segundo)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo a passo do seu programa 
# Passo 1: Entrar no sistema da empresa
# Abriria o navegador
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")
pyautogui.click(x=694, y=593) # clicar na barra de endereços (x e y são as coordenadas da tela)
pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
pyautogui.sleep(3) # tempo de espera para o site carregar (3 segundos)

# Passo 2: Fazer login
# Clicar no campo de email
pyautogui.click(x=-1174, y=379) # clicar no campo de email (x e y são as coordenadas da tela)
pyautogui.write("corvoathano15@gmail.com") # escrever o email
pyautogui.press("tab") 
pyautogui.write("1234554321") # escrever a senha
pyautogui.press("tab") 
pyautogui.press("enter") # clicar no botão de login
# Fazer uma pausa maior para o site carregar
time.sleep(4) # tempo de espera para o site carregar (3 segundos)

# Passo 3: Abrir a base de dados
#pip install pandas openpyxl # bibliotecas para trabalhar com planilhas excel
import pandas

tabela = pandas.read_csv("produtos.csv") # ler a base de dados (planilha excel)
print(tabela) # mostrar a base de dados no terminal

for linha in tabela.index: # para cada linha na base de dados, faça:
  # Passo 4: Cadastrar  produto
  pyautogui.click(x=-1224, y=258) # clicar no campo de email (x e y são as coordenadas da tela)
  codigo = str(tabela.loc[linha, "codigo"]) # pegar o código do produto da linha atual
  pyautogui.write(codigo) # escrever o codigo do produto
  pyautogui.press("tab")

  # Marca
  marca = str(tabela.loc[linha, "marca"]) # pegar a marca do produto da linha atual
  pyautogui.write(marca) # escrever a marca do produto
  pyautogui.press("tab")

  # Tipo
  tipo = str(tabela.loc[linha, "tipo"]) # pegar o tipo do produto da linha atual
  pyautogui.write(tipo) # escrever o tipo do produto
  pyautogui.press("tab")

  # Categoria
  categoria = str(tabela.loc[linha, "categoria"]) # pegar a categoria do produto da linha atual
  pyautogui.write(categoria) # escrever a categoria do produto
  pyautogui.press("tab")
 

  # Preço Unitario
  preco = str(tabela.loc[linha, "preco_unitario"]) # pegar o preço unitário do produto da linha atual
  pyautogui.write(preco) # escrever o preço unitário do produto
  pyautogui.press("tab")

  # Custo
  custo = str(tabela.loc[linha, "custo"]) # pegar o custo do produto da linha atual
  pyautogui.write(custo) # escrever o custo do produto
  pyautogui.press("tab")

  #OBS
  obs = str(tabela.loc[linha, "obs"]) # pegar a observação do produto da linha atual
  if obs != "nan": # se a observação for vazia (nan), escrever "sem observação"
    pyautogui.write(obs) # escrever a observação do produto
  pyautogui.press("tab")

  pyautogui.press("enter") # clicar no botão de cadastrar produto

  # Voltar para o inicio da tela
  pyautogui.scroll(500) # rolar a tela para cima (500 pixels)

# Passo 5: Repetir o passo 4 até acabar a lista de produtos
