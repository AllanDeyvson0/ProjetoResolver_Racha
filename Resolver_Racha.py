print( "\n","--- RESOLVER DIVISÃO DE CONTA IGUALMENTE ---", "\n")
print("SIGA OS PASSOS ABAIXO:","\n")
qt_pessoas = int(input("Informe quantas pessoas irão entrar no racha: "))
print()
print()
lista_p_v = []
for i in range(qt_pessoas):
    print("INSIRA ABAIXO O NOME DA {}° PESSOA:".format(i+1))
    nome = input("Nome: ")
    print("QUAL FOI O VALOR DADO POR {}?".format(nome.upper()))
    valor_dado = float(input("Valor: "))
    print()
    lista_p_v.append([nome.upper(),valor_dado])
valores = []
for x in range(len(lista_p_v)):
    valores.append(lista_p_v[x][1])

print("--- RESULTADOS ABAIXO ---","\n")
print("TOTAL DA CONTA: R$","%.2f"%sum(valores),"\n")
print("[DIVISÃO FEITA IGUALMENTE PRA TODOS]","\n")
print("Quanto ficou pra cada um?")
print("Ficou: R$","%.2f"%(sum(valores)/len(lista_p_v)),"\n","\n")
print("[ABAIXO AS EXCESSÕES DOS VALORES]","\n")
divisao = (sum(valores)/len(lista_p_v))
for t in range(len(valores)):
    if valores[t] < divisao :
        print("{} ainda falta dar: R$".format((lista_p_v[t][0]).upper()),"%.2f"%(divisao - valores[t]))
    elif valores[t] > divisao :
        print("{} falta receber: R$".format((lista_p_v[t][0]).upper()),"%.2f"%(valores[t] - divisao ))
    elif valores[t] == divisao:
        print("{} está quitado.".format((lista_p_v[t][0]).upper()))
print("\n", "--- FIM DO PROBLEMA ---", "\n")
print( "\n","Desenvolvido por ALLAN DEYVSON", "\n")