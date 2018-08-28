import codecs

f = codecs.open('copia.txt', 'r', encoding='latin-1')
n = codecs.open('new.txt', 'w')

for line in f:
    cod = line.replace('\r\n', '').split(';')
    if 'Inativo' not in cod and '2018' in cod:
        n.write(line)


#### para o views.py
# dias = {'SEGUNDA':'2', 'TERÇA':'3', 'QUARTA':'4', 'QUINTA':'5', 'SEXTA':'6'}
# def importar(request):
#     try:
#         f = codecs.open('arq.txt', 'r')
#         f.readline()
#         f.readline()
#         for line in f:
#             formated = line.replace('\n', '').split(';')
#             Id = formated[4]
#             Nome = formated[3]
#             Sexo = formated[6]
#             Profissao = formated[8]
#             EstadoCivil = formated[7]
#             if EstadoCivil == 'VIÚVO':
#                 EstadoCivil = 'VIUVO'
#             Rua = formated[9]
#             Complemento = formated[10]
#             Bairro = formated[11]
#             Cidade = formated[12]
#             Email = formated[13]
#             Fixo = formated[14]
#             Celular = formated[16]
#             Agendamento = int(dias[formated[20]]+formated[21].replace(':00:00', ''))
#             #Modalidade =
#
#         return HttpResponse("Leu")
#     except:
#         return HttpResponse("Erro")
