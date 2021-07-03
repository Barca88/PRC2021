import json

def main() -> ():

    with open('dados.json') as file:
        data = json.loads(file.read())
    
    skeleton = open('skeleton.ttl').read()
    with open('output.ttl', 'w') as out:
        out.write(skeleton)
        out.write("#################################################################\n")
        out.write("#    Individuals\n")
        out.write("#################################################################\n\n")

        for cidade in data['cidades']:
            out.write(f'###  http://www.semanticweb.org/_mark/ontologies/tpc7#{cidade["id"]}\n')
            out.write(f':{cidade["id"]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Cidade ;\n')
            out.write(f'\t\t\t:descrição \"{cidade["descrição"]}\" ;\n')
            out.write(f'\t\t\t:destrito \"{cidade["destrito"]}\" ;\n')
            out.write(f'\t\t\t:nome \"{cidade["nome"]}\" ;\n')
            out.write(f'\t\t\t:população {cidade["população"]} .\n\n')

        for ligacao  in data['ligações']:
            out.write(f'###  http://www.semanticweb.org/_mark/ontologies/tpc7#{ligacao["id"]}\n')
            out.write(f':{ligacao["id"]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Ligação ;\n')
            out.write(f'\t\t\t:temDestino :{ligacao["descrição"]} ;\n')
            out.write(f'\t\t\t:temOrigem :{ligacao["destrito"]} ;\n')
            out.write(f'\t\t\t:distancia {ligacao["nome"]} .\n\n')

if __name__ == "__main__":
    main()