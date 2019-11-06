from matplotlib import pyplot as plt
from clustering import *
import write


def plot(data,clts,cent):
	#define cores para as classes
	colors = ['red','green','blue','orange']
	#cria o objeto figura e atribui ao subplot 1
	fig = plt.figure() 		
	ax = fig.add_subplot(111)
	#define títulos aos eixos
	ax.set_xlabel("carbon")
	ax.set_ylabel("millage")
	#exibe os dados com cores referentes as classes
	for i in range(size):
		plt.scatter(data[i, 0], data[i,1], c = colors[int(clts[i])]) 
	#exibe os centroides 
	plt.scatter(curr_c[:,0],curr_c[:,1], marker='*', s=100, c = 'black')
	plt.show()

write.wrtxt()
plot(data,nearest,curr_c)




