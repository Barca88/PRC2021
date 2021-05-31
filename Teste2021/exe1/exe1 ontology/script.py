import json
import sys

def main(argv):
    size = len(argv)

    if size >= 3:
        imput_file = argv[0]
        output1 = argv[1]
        in_owl = argv[2]
    else: 
        print(size)
        print('ler.json output.owl skeleton.owl')
        return

    with open(imput_file,"r", encoding='utf8') as f:
        dic = json.load(f)

    r = dict()
    r['data'] = dic
    r['output'] = output1
    r['inOwl'] = in_owl
    return r

def toTTL(r):
    data = r['data']
    output = r['output']
    clubes = dict()
    atletas = dict()
    modalidades = dict()

    idAtleta = 1


    file_header = open(r['inOwl']).read()

    with open(output, "w", newline='', encoding='utf-8') as out:
        out.write(file_header) # Classes and Object properties definitions.

        out.write("#################################################################\n")
        out.write("#    Individuals\n")
        out.write("#################################################################\n\n")

        for emd in data:
            #modalidades
            m = emd["modalidade"].replace(' ','_')
            if m not in modalidades:
                modalidades[m] = m
                out.write(f'###  http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{m}\n')
                out.write(f':{m} rdf:type owl:NamedIndividual ,\n')
                out.write(f'\t\t\t\t:Modalidade .\n')
            #clubes
            c = emd["clube"].replace(' ','_')
            if m not in clubes:
                clubes[c] = c
                out.write(f'###  http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{c}\n')
                out.write(f':{c} rdf:type owl:NamedIndividual ,\n')
                out.write(f'\t\t\t\t:Clube .\n')
            #EMD
            id = emd["_id"]
            out.write(f'###  http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{id}\n')
            out.write(f'<http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{id}> rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:EMD ;\n')
            if "dataEMD" in emd: 
                d = emd["dataEMD"]
                out.write(f'\t\t\t:Data "{d}" ;\n')
            if "index" in emd:
                i = emd["index"]
                out.write(f'\t\t\t:Index {i} ;\n')
            if "resultado" in emd:
                r = emd["resultado"]
                out.write(f'\t\t\t:Resultado "{str(r).lower()}"^^xsd:boolean .\n\n')
            #atleta
            mail = emd['email'].replace(' ','_')
            out.write(f"###  http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{mail}\n")
            out.write(f"<http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{mail}> rdf:type owl:NamedIndividual ,\n")
            out.write(f'\t\t\t\t:Atleta ;\n')
            out.write(f'\t\t\t:fezEMD <http://www.semanticweb.org/mark_/ontologies/2021/4/EMD#{id}> ;\n')
            out.write(f"\t\t\t:temClube :{c} ;\n")
            out.write(f"\t\t\t:temModalidade :{m} ;\n")
            f = emd['federado']
            out.write(f"\t\t\t:Federado \"{str(f).lower()}\"^^xsd:boolean ;\n")
            out.write(f"\t\t\t:Genero \"{emd['género']}\" ;\n")
            out.write(f"\t\t\t:Idade {emd['idade']} ;\n")
            out.write(f"\t\t\t:Morada \"{emd['morada']}\" ;\n")
            out.write(f"\t\t\t:Nome \"{emd['nome']['primeiro']}\" ,\n\t\t\t\t\"{emd['nome']['último']}\" ; \n")
            out.write(f"\t\t\t:Primeiro \"{emd['nome']['primeiro']}\" ; \n")
            out.write(f"\t\t\t:Ultimo \"{emd['nome']['último']}\" . \n\n")

if __name__ == "__main__":
    toTTL(main(sys.argv[1:]))