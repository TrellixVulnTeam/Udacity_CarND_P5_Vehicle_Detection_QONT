import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pickle
import functionset as myfc

with open('best_condition.pickle', 'rb') as handle:
    trained_data = pickle.load(handle)

svc = trained_data['model']
X_scale = trained_data['scaler']
orient = trained_data['orient']
pix_per_cell = trained_data['pix_per_cell']
cell_per_block = trained_data['cell_per_block']
spatial_size = trained_data['spatial_size']
hist_bins = trained_data['hist_bins']

myfc.find_cars(200, 600,1, svc, X_scale, orient, pix_per_cell, cell_per_block, spatial_size, hist_bins)