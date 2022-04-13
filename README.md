# Qscraper
Scraper para extração de estatísticas e dados em geral de questões de concursos públicos.

Script com objetivo de extrair dados referentes a questões de concursos públicos do site https://www.tecconcursos.com.br/

Os dados extraídos se referem às matérias das questões, nomes do conteúdos, número de resoluções pelos usuários do site, número de acertos,
ano em que a prova referente a questão foi realizada, se a questão foi anulada, nome da banca que criou a questão, entre outros dados.

Inicialmente, através da biblioteca Selenium, o script inicia uma sessão no navegador chrome, diretamente no site de questões anteriormente
citado. O usuário deste script deve entrar em uma conta no site. A partir daí, deve selecionar um filtro de questões no prórpio site e pressionar
a tecla Enter no terminal. 
