import pandas as pd
import numpy as np

#Number of clusters based on elbow method
k = 4

def read(filename):
	
	data = pd.read_csv(
		filepath_or_buffer= filename,
		dtype = {
			'model' : str,
			'carbon' : np.float64,
			'millage' : np.float64}
	)
	
	#Random centroids initial positions
	centroids_x = data['carbon'].std() * np.random.randn(k) + data['carbon'].mean()
	centroids_y = data['millage'].std() * np.random.randn(k) + data['millage'].mean()

	centroids = np.stack((centroids_x,centroids_y))

	return centroids, data.shape[0]
