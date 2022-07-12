# https://stackoverflow.com/questions/36807701/how-to-get-the-python-counter-output-ordered-by-order-of-inputs
from collections import OrderedDict, Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport, OrderedDict):
    def generate(list):
        resultado = SimpleReport.generate(list)
        empresas = Counter([item["nome_da_empresa"] for item in list])
        resultado += "\nProdutos estocados por empresa:\n"
        for key, value in empresas.items():
            resultado += f"- {key}: {value}\n"
        return resultado
