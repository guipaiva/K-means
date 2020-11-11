import numpy as np
from numpy import linalg as la
from read import *

#Calcula a norma (distancia euclidiana) entre dois arrays
#axis = 1 significa que será utilizado o eixo horizontal para cálculo, considerando elementos de mesma linha
def distance(a,b, ax = 1):
	return la.norm((a-b),axis = ax)

#inicia a lista de distancias como zero, no formato [80]X[3], neste caso
distances = np.zeros((size,k))

#Lista para histórico de posições de centroides
c_history = []

#Posição atual da centroide
curr_c = centroids
c_history.append(curr_c)

#Variável de controle para critério de parada do programa
error = 1

#Critério de parada = 0
while error > 0:
	
	#Calcula a distancia entre as centroides e todos os pontos
	for i in range(size):
		distances[i] = distance(data[i],centroids)
	
	#Define as posições onde as distances são menores para cada centroide
	nearest = np.argmin(distances, axis = 1)

	#Atualiza o centróide atual para a média das posições onde a distancia é menor 
	for i in range(k):
		curr_c[i] = np.mean(data[nearest == i], axis = 0)

	#adiciona ao histórico as posições atuais da centroides
	c_history.append(curr_c)

	'''Calcula a movimentação da centroide baseado na distância entre 
	a centroide atual e sua ultima posição'''  
	error = distance(curr_c, c_history[-1], None)

c_history = np.array(c_history, dtype='f')

	 
