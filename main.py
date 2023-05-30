import tkinter

from antlr4 import *

from gen.NoticiaLexer import NoticiaLexer
from gen.NoticiaParser import NoticiaParser
import requests
from bs4 import BeautifulSoup


import requests
from bs4 import BeautifulSoup
from tkinter import *


def PickNewsInPost(news):
  news_list = ""
  for new in news:
    news_list += (new.get_text()+'\n')
  return news_list

def PickNewsInPage(link):
  # Fazendo uma requisição para o servidor do site
  second_request = requests.get(link)

  if second_request.status_code == 200:
    second_soup = BeautifulSoup(second_request.content, 'html.parser')
    corpo_noticia = second_soup.find('div', class_='post-body')
    noticia = second_soup.find('h1', class_='post-title').get_text()+'\n'
    noticia += PickNewsInPost(corpo_noticia.find_all('p'))
    with open('input.txt', 'w+', encoding='utf8') as f:
        f.write(noticia)
    return noticia


def get_text():
    # Função chamada quando o botão é clicado
    text = entry.get()  # Obtém o texto digitado no campo de entrada
    print(text)
    return text

def antlr():
    dados = FileStream('input.txt', encoding='utf-8')
    #dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = NoticiaLexer(dados)
    # for tok in lexer.getAllTokens():
    #     print(tok.text, tok.type)
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = NoticiaParser(stream)
    tree = parser.ini()
    print(tree.toStringTree())
    return tree.toStringTree()

def buttonPressed():
    PickNewsInPage(get_text())
    tx = Text(janela, width=60)
    # texto_resposta = Label(janela, text=antlr())
    # texto_resposta.grid(column=0, row=2, padx=10, pady=10)
    tx.insert(END, antlr())
    tx.grid(column=0, row=2, padx=10, pady=10)

if __name__ == '__main__':
    # PickNewsInPage()
    janela = Tk()
    janela.geometry('500x500')
    janela.title("Analisador léxico de notícias")
    texto = Label(janela, text="Coloque aqui o link da notícia desejada no site https://cidadeverde.com/")
    texto.grid(column=0, row=0, padx=10, pady=10)

    entry = Entry(janela)  # Cria um campo de entrada de texto
    entry.grid(column=0, row=1, padx=10, pady=10)  # Posiciona o campo de entrada na janela

    button = Button(janela, text="Enviar", command=buttonPressed)  # Cria um botão
    button.grid(column=1, row=1, padx=10, pady=10)  # Posiciona o botão na janela

    janela.mainloop()
