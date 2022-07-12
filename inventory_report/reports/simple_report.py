from datetime import date
from collections import Counter


class SimpleReport:
    def generate(list):
        lista_data_fabricacao = []
        lista_data_validade = []
        lista_nome_empresas = []

        for element in list:
            if ("data_de_validade" in element.keys()):
                lista_data_fabricacao.append(element["data_de_fabricacao"])
                ano, mes, dia = element["data_de_validade"].split('-')
                lista_data_validade.append(date(int(ano), int(mes), int(dia)))
                lista_nome_empresas.append(element["nome_da_empresa"])

        nova_lista = [
            data for data in lista_data_validade if data >= date.today()
        ]

        validade_mais_proxima = min(
            nova_lista, key=lambda sub: abs(sub - date.today())
        )

        empresa, quantidade = Counter(
            nome for nome in lista_nome_empresas
        ).most_common(1)[0]

        result = (
            f"Data de fabricação mais antiga: {min(lista_data_fabricacao)}\n"
            f"Data de validade mais próxima: {validade_mais_proxima}\n"
            f"Empresa com mais produtos: {empresa}"
        )
        return result
