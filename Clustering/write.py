from read import models
from clustering import nearest, curr_c


def wrtxt():
	#Cria uma lista com os modelos e suas classes respectivamente
	classes = [[i,j] for i,j in zip(models,nearest)]

	#Lista com o texto a ser inserido no arquivo txt
	lines = []
	for i in range(len(curr_c)):
		lines.append('Classe '+str(i)+'\nMédia de emissão de carbono: '+str(curr_c[i][0])+'\n')
		lines.append('Média de emissão de consumo: '+str(curr_c[i][1])+'\n\n')

	#Cria o arquivo classes.txt e escreve nele, os dados acima
	w = open('classes.txt', 'w', newline = '\n')
	w.writelines(lines)



	w.close()