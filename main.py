from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome('/home/zskyver/PycharmProjects/WebCrawler/chromedriver', chrome_options=options)


def buscador():
    busca = input(str("digite a sua busca: "))
    busca.replace(" ", "%20")
    driver.get("https://www.google.com/search?q=" + busca)
    return driver


def tratamento_de_texto(buscador):
    links = []
    results = buscador.find_elements_by_class_name("g")
    print(len(results))

    for i in range(len(results)):
        links.append(str(results[i].find_element_by_tag_name("a").get_attribute("href")))

    contador = 0


    for link in links:
        if link.__contains__("http"):
            buscador.get(link)
            textos = buscador.find_elements_by_tag_name("p")
            f = open("%s.txt" % contador, "w")
            contador_paragrafos = 0
            for contador_paragrafos in range(len(textos)):
                f.write(textos[contador_paragrafos].text)
        contador = contador + 1
        f.close()
        print("Arquivo criado!")
    buscador.quit()
    pass


tratamento_de_texto(buscador())
