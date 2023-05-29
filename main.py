from antlr4 import *

from gen.NoticiaLexer import NoticiaLexer
from gen.NoticiaParser import NoticiaParser
import requests
from bs4 import BeautifulSoup


def PickNewsInPost(news):
    news_list = ""
    for new in news:
        news_list += (new.get_text() + "\n")
    return news_list

def PickingNews():
    # Fazendo uma requisição para o servidor do site
    r = requests.get("https://cidadeverde.com/ultimas")

    # Verificando se a requisição foi bem sucedida
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        first_soup = soup.find_all('h4')[1]
        link = first_soup.find('a')
        # print(link.get('href'))
        second_request = requests.get(link.get("href"))
        if second_request.status_code == 200:
            second_soup = BeautifulSoup(second_request.content, 'html.parser')
            corpo_noticia = second_soup.find('div', class_='post-body')
            noticia = second_soup.find('h1', class_='post-title').get_text() + '\n'
            noticia += PickNewsInPost(corpo_noticia.find_all('p'))
            with open('input.txt', 'w', encoding="utf-8") as file:
                text = noticia.encode('utf-8').decode('ascii', errors='ignore')
                file.write(text)


if __name__ == '__main__':
    PickingNews()
    dados = FileStream('input.txt')
    #dados = InputStream("hello Raimundo, Santos, Moura.")
    lexer = NoticiaLexer(dados)
    # for tok in lexer.getAllTokens():
    #     print(tok.text, tok.type)
    lexer.reset()
    stream = CommonTokenStream(lexer)
    parser = NoticiaParser(stream)
    tree = parser.ini()
    print(tree.toStringTree())
