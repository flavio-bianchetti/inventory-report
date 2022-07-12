import csv
import json

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory(CompleteReport, SimpleReport):
    def import_data(caminho, tipo):
        dados = Inventory.get_file_data(caminho)
        resultado = ""
        if tipo == "simples":
            resultado = SimpleReport.generate(dados)
        if tipo == "completo":
            resultado = CompleteReport.generate(dados)
        return resultado

    def get_file_data(caminho):
        extensao = caminho.split(".")[-1]
        print(extensao.upper())
        resultado = ""
        if extensao.upper() == "CSV":
            resultado = Inventory.get_file_csv(caminho)
        if extensao.upper() == "JSON":
            resultado = Inventory.get_file_json(caminho)
        return resultado

    def get_file_csv(caminho):
        try:
            lista_de_produtos = []
            with open(caminho, encoding="utf-8") as file:
                dados = csv.DictReader(file, delimiter=",", quotechar='"')
                for row in dados:
                    lista_de_produtos.append(row)
                return lista_de_produtos
        except IOError:
            print("Error: o arquivo não existe.")
            return
        except Exception:
            print("Error: dados inválidos.")
            return

    def get_file_json(caminho):
        try:
            lista_de_produtos = []
            with open(caminho) as file:
                dados = json.load(file)
                for row in dados:
                    lista_de_produtos.append(row)
                return lista_de_produtos
        except IOError:
            print("Error: o arquivo não existe.")
            return
        except Exception:
            print("Error: dados inválidos.")
            return
