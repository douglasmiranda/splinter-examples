# -*- coding: utf-8 -*-
"""
 Exemplo para uso no artigo de meu website:
 http://douglasmiranda.com/artigo/teste-interface-de-sua-aplicacao-web-no-melhor-estilo-ninja-de-testes-com-splinter/

 O objetivo é:
 - visitar meu website
 - fazer uma busca com a palavra-chave "python"
 - e verificar se há resultados
"""
import time
from splinter.browser import Browser
# Se eu não passar nenhum driver, Browser(),
# o padrão já será o firefox.
browser = Browser('firefox')

url = "http://douglasmiranda.com"
# Na linha abaixo eu visito a url,
# é neste momento em que o browser se abrirá
browser.visit(url)
# com o método fill eu preencho o campo de formulário,
# ele encontra este campo pelo atributo name do input
# para interagir com elementos veja mais formas em:
# http://splinter.cobrateam.info/docs/elements-in-the-page.html
palavra_chave = "python"
browser.fill('q', palavra_chave)

# estou inserindo este delay aqui porque ao preencher o campo de busca
# há uma animação no botão "Pesquisar", este é o tempo para que
# a animação esteja completa e o botão esteja clicável
# que é um ponto importante, pois o objeto precisa estar visível para
# que ele possa ser clicado
time.sleep(0.2)

# Encontrando o botão de submit do formulário
# que é um <input type="submit"... dentro de um
# formulário que tem o id="search-form"
# por um seletor CSS, se você é familiarizado
# com CSS vai achar bem simples o uso
# mais formas de encontar elementos na página em:
# http://splinter.cobrateam.info/docs/finding.html
botao_pesquisar = browser.find_by_css("#search-form input[type=submit]")
# Veja que ao encontrar o botão eu posso interagir com ele
# neste caso "estou clicando" nele, que vai submeter meu
# formulário #search-form, enviando a palavra "python" para ser
# pesquisada em meu banco de dados
botao_pesquisar.click()

# com o método is_element_present_by_id vou checar se apareceu
# a lista de posts que tem o id="posts-list"
# mais formas checar textos e elementos presentes no corpo da página em:
# http://splinter.cobrateam.info/docs/matchers.html
if browser.is_element_present_by_id('posts-list'):
	print "Oh yes! Já escrevi artigos sobre '%s'! =D" % palavra_chave
else:
	print "Não escrevi nenhum artigo sobre '%s'? OMG!" % palavra_chave

# Ao término eu fecho o browser
browser.quit()