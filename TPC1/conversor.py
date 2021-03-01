import json

with open('data.json', 'r') as f:
    d = f.read()

data = json.loads(d)

fich = open("dados.ttl", "w")

for i in data['alunos']: 
    fich.write('### http://prc.di.uminho.pt/2021/uc#' + str(i["id"]) + '\n')
    fich.write(':' + str(i["id"]) + ' rdf:type owl:NamedIndividual ,\n')
    fich.write('\t\t\t\t:Aluno ;\n')
    fich.write('\t\t:frequenta :' + str(i["frequenta"]) + ' ;\n')
    fich.write('\t\t:nome \"' + str(i["nome"]) + '\" .\n')
    fich.write('\n\n')

for i in data['docentes']: 
    fich.write('### http://prc.di.uminho.pt/2021/uc#' + str(i["id"]) + '\n')
    fich.write(':' + str(i["id"]) +' rdf:type owl:NamedIndividual ,\n')
    fich.write('\t\t\t\t:Professor ;\n')
    fich.write('\t\t:ensina :' + str(i["ensina"]) + ' ;\n')
    fich.write('\t\t:nome \"' + str(i["nome"]) + '\" .\n')
    fich.write('\n\n')

for i in data['ucs']: 
    fich.write('### http://prc.di.uminho.pt/2021/uc#' + str(i["id"]) + '\n')
    fich.write(':' + str(i["id"]) +' rdf:type owl:NamedIndividual ,\n')
    fich.write('\t\t\t\t:UnidadeCurricular ;\n')
    fich.write('\t\t:anoLetivo \"' + str(i["anoLetivo"]) + '\" ;\n')
    fich.write('\t\t:designação \"' + str(i["designação"]) + '\" .\n')
    fich.write('\n\n')


fich.close()


f.close()