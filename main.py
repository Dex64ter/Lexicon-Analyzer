from antlr4 import *

from gen.NoticiaLexer import NoticiaLexer
from gen.NoticiaParser import NoticiaParser

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
    text = inp.get()  # Obtém o texto digitado no campo de entrada
    print(text)
    return text

def antlr():
    dados = FileStream('input.txt', encoding='utf-8')
    #dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = NoticiaLexer(dados)
    types = {  ## Retirado do arquivo Lexer
        1: "P.R. (Palavra reservada)",
        2: "Espaço ou parágrafo",
    }
    expr = ('{0:16} | {1:25}'.format("Token", "Tipo"))
    expr += ('-' * 46)
    expr += '\n'
    for tok in lexer.getAllTokens():
        expr += ('{0:16} | {1:28}'.format(tok.text, types[tok.type])) + '\n'
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = NoticiaParser(stream)
    tree = parser.ini()
    print(tree.toStringTree())
    return (expr + "Parser Tree:\n" + tree.toStringTree())

def buttonPressed():
    PickNewsInPage(get_text())
    janela.geometry("500x500")
    tx = Text(janela, wrap="word")
    tx.insert(END, antlr())
    tx.pack(fill=BOTH)

if __name__ == '__main__':
    janela = Tk()
    janela.geometry("500x100")
    janela.title("Analisador léxico de notícias")
    tit = Label(janela, text="Link da notícia do site https://cidadeverde.com/")
    inp = Entry()
    but = Button(janela, text="Enviar", width=25,height=1,command=buttonPressed)

    tit.pack(fill=BOTH)
    inp.pack(fill=BOTH)
    but.pack()
    janela.mainloop()
