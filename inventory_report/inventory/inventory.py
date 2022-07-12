import csv

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(CompleteReport, SimpleReport):
    def import_data(caminho, tipo):
        lista_de_produtos = []
        with open(caminho, encoding="utf-8") as file:
            dados = csv.DictReader(file, delimiter=",", quotechar='"')
            print(dados)
            resultado = ""
            for row in dados:
                lista_de_produtos.append(row)
            if tipo == "simples":
                resultado = SimpleReport.generate(lista_de_produtos)
            if tipo == "completo":
                resultado = CompleteReport.generate(lista_de_produtos)
            return resultado
