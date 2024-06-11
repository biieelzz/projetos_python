import pyautogui
import pyperclip
import webbrowser
import time
import yfinance

# criando uma váriavel para receber o código da ação a ser analisada
ticker = input("Digite o código da ação desejada: ")
data_inicio = input("Digite a data inicial (padrão AAAA-MM-DD) para análise: ")
data_fim = input("Digite a data final (padrão AAAA-MM-DD) para análise: ")

# guardando os dados a serem analisados em variáveis
dados = yfinance.Ticker(ticker).history(start=data_inicio, end=data_fim)
fechamento = dados.Close

# calculando os valores máximos, mínimos e média
maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
valor_medio = round(fechamento.mean(), 2)

# criando as variáveis para envio do e-mail
destinatario = input("Digite o e-mail do destinatário: ")
assunto = "Análises de ações"
mensagem = f"""
Prezado Gestor,

Seguem as análises solicitadas da ação {ticker}:

Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Valor médio: R${valor_medio}

Qualquer dúvida, estou à disposição!

Atte.
"""

# abrir o navegador e ir para o Gmail
webbrowser.open("www.gmail.com")
time.sleep(3)

# configurando uma pausa de 3 segundos do pyautogui
pyautogui.PAUSE = 3

# clicar no botão Escrever
pyautogui.click(x=190, y=200)

# digitar o e-mail do destinatário e teclar TAB
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar o assunto do e-mail e teclar TAB
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# digitar a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# clicar no botão Enviar
pyautogui.click(x=1310, y=1000)

# fechar aba do Gmail
pyautogui.hotkey("ctrl", "f4")

print("E-mail enviado com sucesso!")