from leitorarquivo import LeitorArquivo

import numpy as np
import matplotlib.pyplot as plt

def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)

    plt.ylabel('Valores de entrada')
    plt.xlabel('Amostragem')
    plt.title('Gráfico de linhas')

    i = 1
    for serie in valores:
        plt.plot(serie, label='Série ' + str(i))   
        i += 1
    plt.legend(loc='upper left')



    plt.subplot(1, 2, 1)


    plt.xlabel('Valores de entrada')
    plt.ylabel('Amostragem')    
    plt.title('Gráfico de linhas')


    i = 1
    for serie in valores:
        plt.plot(serie, label = 'Série ' + str(i))
        i += 1
    plt.legend(loc='upper left')


    #Plotando gráfico de barras (médias)
    plt.subplot(1, 2, 2)
   
    medias = leitor.getMedias()
    xvalues = np.arange(1, len(medias)+1)
    plt.bar(xvalues, medias)  
    plt.xticks(xvalues, ['Série ' + str(x) for x in xvalues])
    plt.title('Médias das séries')
    plt.show()
main()