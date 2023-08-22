import xmltodict
import os
import pandas as pd

def pegar_infos(nome_arquivo, valores):
    with open(f"nfs/{nome_arquivo}", "rb") as arquivo_xml:
        dict_arquivo = xmltodict.parse(arquivo_xml)
        if "NFe" in dict_arquivo:
            infos_nf = dict_arquivo["NFe"]["infNFe"]
        else:
            infos_nf = dict_arquivo["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infos_nf["@Id"]
        empresa_emissora = infos_nf["emit"]["xNome"]
        nome_cliente = infos_nf["dest"]["xNome"]
        endereco = infos_nf["dest"]["enderDest"]
        if 'vol' in infos_nf["transp"]:
            peso = infos_nf["transp"]["vol"]["pesoB"]
        else:
            peso = "Não informado"
        valores.append([numero_nota,empresa_emissora,nome_cliente,endereco,peso])


list_arquivos = os.listdir("nfs")
colunas = ["numero_nota","empresa_emissora","nome_cliente","endereco","peso"]
valores = []

for arquivo in list_arquivos:
    pegar_infos(arquivo,valores)

tabela = pd.DataFrame(columns=colunas,data=valores)
print(tabela)
tabela.to_excel("NotasFiscais.xlsx", index=False)