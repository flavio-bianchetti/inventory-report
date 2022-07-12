import csv
import json
from xml.etree import cElementTree as ET

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
        resultado = ""
        if extensao.upper() == "CSV":
            resultado = Inventory.get_file_csv(caminho)
        if extensao.upper() == "JSON":
            resultado = Inventory.get_file_json(caminho)
        if extensao.upper() == "XML":
            resultado = Inventory.get_file_xml(caminho)
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

    # https://docs.python.org/pt-br/3/library/xml.etree.elementtree.html?highlight=xml#xml.etree.ElementTree.XML
    def get_file_xml(caminho):
        try:
            lista_de_produtos = []
            with open(caminho) as file:
                tree = ET.parse(file)
                dados = tree.getroot()
                for row in dados.findall("record"):
                    produto = {
                        "id": int(row.find("id").text),
                        "nome_do_produto": row.find("nome_do_produto").text,
                        "nome_da_empresa": row.find("nome_da_empresa").text,
                        "data_de_fabricacao": row.find(
                            "data_de_fabricacao"
                        ).text,
                        "data_de_validade": row.find("data_de_validade").text,
                        "numero_de_serie": row.find("numero_de_serie").text,
                        "instrucoes_de_armazenamento": row.find(
                            "instrucoes_de_armazenamento"
                        ).text,
                    }
                    lista_de_produtos.append(produto)
                return lista_de_produtos
        except IOError:
            print("Error: o arquivo não existe.")
            return
        except Exception:
            print("Error: dados inválidos.")
            return
