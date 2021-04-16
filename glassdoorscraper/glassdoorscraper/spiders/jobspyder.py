import scrapy

def palabras_clave():
    """Permite al usuario seleccionar las palabras clave que
    se usarán en la búsqueda.
    """
    keywords = input("Select keywords: ")
    keywords = keywords.split()
    words = ""
    for word in keywords:
        words += (word + "+")
    keywords = words[:-1]
    return keywords

lista_de_keywords = []

seguir_buscando = True

while seguir_buscando:
    keywords = palabras_clave()
    lista_de_keywords.append(keywords)
    if keywords == "stop":
        seguir_buscando = False

lista_de_trabajos = []

for keyword in lista_de_keywords:
    link = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=N&locId=3&jobType="
    lista_de_trabajos.append(link)

class GlassdoorJob(scrapy.Spyder):
    name = "job"
    start_url = lista_de_trabajos

    def parse(self, response):
        for link in lista_de_trabajos:
            yield {
                'job' = response.css('h1.hideHH.css-zga872.e15r6eig0::text').get(),
            }
