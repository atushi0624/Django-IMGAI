from django.db import models
from img.lib import img_predict
import os
import tensorflow as tf

# Create your models here.

class ImageFiles(models.Model):

    image = models.ImageField(upload_to='img')

    global graph
    graph = tf.get_default_graph()

    def get_filename(self):
        return os.path.basename(self)

    def get_path(self):
    	path_name = '/media/'
    	file_name = path_name + str(self.image)
    	return file_name

    def get_predict(self):
    	path_name = 'media/'
    	file_name = path_name + str(self.image)
    	
    	with graph.as_default():
    		predict = img_predict.img_predict(file_name)
    		percent = predict['percent']

    	if predict['result'] == 0:
    		result = "ポテトチップス"
    	if predict['result'] == 1:
    		result = "コーラ"
    	if predict['result'] == 2:
    		result = "カップヌードル"

    	context = [result,percent]

    	return context
