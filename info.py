# -*- coding: utf-8 -*-

import bs4, requests

Info={
     'madonnaDellaStella':'https://www.iatgravina.it/chiesa-rupestre-della-madonna-della-stella/',
     'ponte':'https://www.iatgravina.it/ponte-acquedotto-madonna-della-stella/',
     'bastione':'https://www.iatgravina.it/bastione-medievale/',
     'sanFrancesco':'https://www.iatgravina.it/chiesa-convento-e-chiostro-di-san-francesco/',
     'castello':'https://www.iatgravina.it/castello-svevo-di-federico-ii/',
     'santaSofia':'https://www.iatgravina.it/chiesa-convento-e-chiostro-di-santa-sofia/',
     'santaLucia':'https://www.cartapulia.it/dettaglio?id=127647',
     'sanBasilio':'https://www.cartapulia.it/dettaglio?id=127826',
     'purgatorio':'https://www.iatgravina.it/chiesa-santa-maria-del-suffragio-purgatorio/',
     'palazzoOrsini':'https://www.cartapulia.it/dettaglio?id=126083',
     'museoCivico':'https://www.iatgravina.it/museo-fondazione-ettore-pomarici-santomasi/',
     'statuaPapa':'https://www.iatgravina.it/statua-papa-benedetto-xiii/',
     'cattedrale':'https://www.iatgravina.it/basilica-cattedrale-di-santa-maria-assunta/',
     'sanMichele':'https://www.iatgravina.it/chiesa-rupestre-di-san-michele-delle-grotte-e-rione-fondovito/',
     'bibliotecaFinya':'https://www.iatgravina.it/biblioteca-finya/',
     'quattroFontane':'https://www.iatgravina.it/fontana-ferdinandea-de-le-quattro-fontane/',
     'torreOrologio':'https://www.iatgravina.it/torre-dellorologio-e-monumento-ai-caduti/',
     }


def get_info(nome):
    pre_link="https://www.cartapulia.it/dettaglio?id="
    link=Info[nome]
    response=requests.get(link)
    soup =bs4.BeautifulSoup(response.text, 'html.parser')
    
    if pre_link in link:
        text_search=soup.find('div', class_='u-margin-bottom-l u-padding-all-xxs')
    else:
        text_search=soup.find('div', class_='wpb_wrapper')
    text=text_search.find_all('p')
    lista_text=[]
    
    for testo in text:
        lista_text.append(str(testo))
      
    if nome=='palazzoOrsini' or nome=='castello' or nome=='sanBasilio':
        return lista_text[1]
    else:
        return lista_text[0]


