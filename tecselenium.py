import json
from lxml import html
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests as r



materias = ['AFO, Direito Financeiro e Contabilidade Pública', 'Administração Geral', 'Administração Pública', 'Administração Geral e Pública', 'Análise das Demonstrações Contábeis', 'Auditoria Governamental e Controle',
'Auditoria Privada', 'Contabilidade de Custos', 'Contabilidade de Instituições Financeiras e Atuariais', 'Contabilidade Geral', 'Direito Administrativo', 'Direito Civil',
'Direito Constitucional', 'Direito Econômico', 'Direito Empresarial (Comercial)', 'Direito Penal', 'Direito Tributário', 'Economia e Finanças Públicas', 'Estatística', 
'Ética no Serviço Público', 'Finanças e Conhecimentos Bancários', 'Informática', 'Legislação Aduaneira', 'Legislação Geral Estadual e do DF', 'Legislação Geral Federal',
'Legislação Tributária dos Estados e do Distrito Federal', 'Legislação Tributária dos Municípios e do Distrito Federal', 'Legislação Tributária Federal', 'Matemática Financeira',
'Português', 'Raciocínio Lógico', 'Matemática', 'TI - Banco de Dados']

del_keys = ["uuidLogoOrgao", "orgaoNome", "caminhoLogotipoOrgao", "cargoNome", "concursoArea", "concursoEdicao", "dataPublicacao", "questaoProva", "questaoDificuldade", "questaoNumero", 
"porcentagemAcertos", "demaisConcursos", "porcentagemErros"]

headers2 = {
    'accept': 'application/json, text/plain, * / *',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'pt-BR,pt;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    'cookie': '_ga=GA1.3.1596892190.1645445484; _gid=GA1.3.1377822667.1648846580; busca-por-enunciado-usuario-687871={%22busca%22:%22#1700000%22%2C%22questao%22:1700000}; busca-por-enunciado-usuario-2749304={%22busca%22:%22#1000%22%2C%22questao%22:1000}; TecPermanecerLogado=Mjc1OTA1NyxwZ2Nvc3RhZkBnbWFpbC5jb20sJDJhJDEyJEIyaFlpZkVwVmQ2QXNsNkppSjFCVmVNNWpwN2ZkQ3UxN2VmMVo1Y3F5RHAwWG1WN3RjOURX; JSESSIONID=9902B21ED3676BB7B0E91855D34C6A42; AWSALB=SZ9NaVkNnkjCtrwvTMTkA6/d/iCxmYXt+Ee64kq7MWNBy4HXVy/Tm6ukaAg5vmQ7fpj7TTjaXvTXOILOAOdu/YYF21xU3YGp/0LkZB1A8FAwnEEQ+LAQbw8L9qpR; AWSALBCORS=SZ9NaVkNnkjCtrwvTMTkA6/d/iCxmYXt+Ee64kq7MWNBy4HXVy/Tm6ukaAg5vmQ7fpj7TTjaXvTXOILOAOdu/YYF21xU3YGp/0LkZB1A8FAwnEEQ+LAQbw8L9qpR',
    'if-modified-since': 'Mon, 26 Jul 1997 05:00:00 GMT',
    'logado': 'true',
    'pragma': 'no-cache',
    'referer': 'https://www.tecconcursos.com.br/questoes/busca',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    }

url = "https://www.tecconcursos.com.br/questoes/filtrar"


driver = webdriver.Chrome( executable_path=r'C:\Users\user\Documents\Chromedriver\chromedriver.exe')
driver.get(url)

#######################################################################################################
input("Entre na sua conta do TecConcursos, crie um filtro de questões e aperte Enter...")
#######################################################################################################

for i in range(100000):

    try:
        materia = driver.find_element(by=By.CSS_SELECTOR, value='#ancora-filtro-questao > div > div:nth-child(8) > div > section.questao-cabecalho > div.questao-cabecalho-informacoes > div.questao-cabecalho-informacoes-materia.espacamento-3 > a').text

        id  = driver.find_element(by=By.CSS_SELECTOR, value='#ancora-filtro-questao > div > div.ng-isolate-scope > div > section.questao-rg-area.espacamento-3 > div > header > div > a').text
        id = id.replace("#", '')

        time.sleep(3)

        qinfos_url = 'https://www.tecconcursos.com.br/api/questoes/'+str(id)+'/detalhes'

    
        res2 = r.get(qinfos_url)

        search_cookies2 = res2.cookies
        
        session = r.Session()
        res_get2 = session.get(qinfos_url, cookies=search_cookies2, headers=headers2)        
        
        timeout = time.time() + 5
        while res_get2.status_code != 200:
            res_get2 = session.get(qinfos_url, cookies=search_cookies2, headers=headers2)
            if time.time() > timeout:
                break        

        qinfos = res_get2.content.decode()        
        
        try:
            qinfos = json.loads(qinfos)

            if qinfos["informacoes"]["totalQuestaoResolvida"] >= 100:


                try:
                    qinfos = qinfos["informacoes"]
                except:
                    None
                
                for j in range(len(del_keys)):
                    try:
                        del qinfos[del_keys[j]]
                    except:
                        None
                
                
                with open('qinfos.json', 'r+') as file:
                    data = json.load(file)
                    data["qinfos"].append(qinfos)
                    file.seek(0)
                    json.dump(data, file, indent=4)

        except ValueError:
            print('Decoding JSON has failed')

    except:
        None

    driver.find_element(by=By.CSS_SELECTOR, value='#ancora-filtro-questao > div > div:nth-child(8) > div > article > div.questao-enunciado-resolucao > div > button.questao-navegacao-botao.questao-navegacao-botao-proxima').click()
    time.sleep(4)
    
    i = i+1