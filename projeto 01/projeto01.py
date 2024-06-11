# Projeto 01 - Criar um Orçamento em PDF

from fpdf import FPDF

# capturar as informações sobre o orçamento
projeto = input("Digite a descrição do projeto: ")
horas_previstas = input("Digite a quantidade de horas previstas: ")
valor_hora = input("Digite o valor da hora trabalhada: ")
prazo = input("Digite o prazo estimado: ")

# realizar o cálculo do valor total
valor_total = int(horas_previstas) * int(valor_hora)

# criar um PDF em branco
pdf = FPDF()

# adicionar uma página e setar uma fonte
pdf.add_page()
pdf.set_font("Arial")

# inserir um layout de fundo
pdf.image("template.png", x=0, y=0)

# inserir as informações do orçamento dentro do PDF
pdf.text(115, 145, projeto)
pdf.text(115, 160, horas_previstas)
pdf.text(115, 175, valor_hora)
pdf.text(115, 190, prazo)
pdf.text(115, 205, str(valor_total)) # pdf só aceita variáveis em string

# gerar o arquivo finalizado
pdf.output("Orçamento.pdf")
print("Orçamento gerado com sucesso!")