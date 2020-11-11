import csv
import numpy as np

'''Define o numero de centróides para 3, este número foi escolhido baseado no método cotovelo
que está explicado no pdf que segue junto ao trabalho'''
k = 4
#carrega o arquivo e atribui às variáveis
f = open('data.txt','r')
reader = csv.reader(f, delimiter = ',')
next(f)
data = np.array(list(reader))
f.close()

#Separa as strings dos dados em arrays diferentes
models = np.array(data[:,0])
carbon = np.array(data[:,1], dtype = 'float')
millage = np.array(data[:,2], dtype = 'float')

#Média dos valores de carbon e millage
mean_x = np.mean(carbon)
mean_y = np.mean(millage)

#Desvio Padrão dos valores de carbon e millage
std_dev_x = np.std(carbon)
std_dev_y = np.std(millage)


#Gera posições x e y aleatórias a partir de uma distribuição normal
c_x = np.random.randn(k)* std_dev_x + mean_x
c_y = np.random.randn(k)* std_dev_y + mean_y

#Define as coordenadas iniciais da centroides a partir dos dados anteriores
centroids = np.array(list(zip(c_x, c_y)), dtype='float')

#Define a variável data com todas os valores de carbon e millage
data = np.array(list(zip(carbon,millage)), dtype = 'float')

#número de dados
size = len(data)
