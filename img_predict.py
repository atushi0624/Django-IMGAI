def img_predict(file_name):
	#ライブラリの読み込み
	from keras.models import Sequential,load_model
	from keras.layers import Conv2D, MaxPooling2D
	from keras.layers import Activation, Dropout, Flatten, Dense
	from keras.utils import np_utils
	import keras
	import numpy as np

	from PIL import Image
	import os, glob

	#クラスの定義
	classes = ["potetochipes","cola","cupnoodle"]
	num_classes = len(classes)
	image_size = 50

	#予測データの読み込み
	file =  file_name
	image = Image.open(file)
	image = image.convert("RGB")
	image = image.resize((image_size, image_size))
	data = np.asarray(image)
	x=[]
	x.append(data)
	X=np.array(x)

	#モデルの定義
	model = Sequential()
	model.add(Conv2D(32,(3,3), padding='same',input_shape=(50,50,3)))
	model.add(Activation('relu'))
	model.add(Conv2D(32,(3,3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))

	model.add(Conv2D(64,(3,3), padding='same'))
	model.add(Activation('relu'))
	model.add(Conv2D(64,(3,3)))
	model.add(Activation('relu'))
	model.add(MaxPooling2D(pool_size=(2,2)))
	model.add(Dropout(0.25))

	model.add(Flatten())
	model.add(Dense(512))
	model.add(Activation('relu'))
	model.add(Dropout(0.5))
	model.add(Dense(3))
	model.add(Activation('softmax'))

	opt = keras.optimizers.rmsprop(lr=0.0001, decay=1e-6)
	model.compile(loss='categorical_crossentropy',optimizer=opt,metrics=['accuracy'])

	#モデルをロード
	model= load_model('img/lib/img_cnn.h5')
	#画像判定結果を表示
	result = model.predict([X])[0]
	yosoku = result.argmax()
	percent = int(result[yosoku]*100)
	predict_result = []
	predict_result = { 'result':yosoku,'percent':percent }

	return  predict_result
