import keras
import numpy as np
from PIL import Image
from traitement_images import traitement_images
#Création du modele
vgg16_features = keras.applications.vgg16.VGG16(include_top=False, weights='imagenet')
vgg16_features.save("vgg16Q2_2_et_3.h5")
vgg16_features = keras.models.load_model("vgg16Q2_2_et_3.h5")
vgg16_features.trainable = True

from keras.layers import Input, Dense, Flatten, Model, Dropout

inputs = Input(shape=(224,224,3))
out_vggfeatures = vgg16_features(inputs)
couche_aplatissement = Flatten()(out_vggfeatures)
couche_dense = Dense(512, activation='relu')(couche_aplatissement)
couche_dropout = Dropout(0.25)(couche_dense)
couche_dense2 = Dense(512, activation='relu')(couche_dropout)
couche_dropout2 = Dropout(0.25)(couche_dense2)
predictions = Dense(3, activation='softmax')(couche_dropout2)

model = Model(inputs=inputs, outputs = predictions)

model.summary()

model.compile(optimizer=keras.optimizers.SGD(lr=1e-4, momentum=0.9), loss='categorical_crossentropy', metrics = ['accuracy'])


import multiprocessing

cpu = 8  # Put the correct amount

manager = multiprocessing.Manager()


x_train = manager.list()
y_train = manager.list()
x_test = manager.list()
y_test = manager.list()

def creation_jeux(i):
    nom_fichier = '../donnees/generated/BMW/bmw' + str(i) + '.jpg'
    nom_fichier2 = '../donnees/generated/Mercedes/mercedes' + str(i) + '.jpg'
    nom_fichier3 = '../donnees/generated/Audi/audi' + str(i) + '.jpg'
    if (i < 3200):
        x_train.append(traitement_images(nom_fichier)[0])
        y_train.append([1,0,0])
        x_train.append(traitement_images(nom_fichier2)[0])
        y_train.append([0,1,0])
        x_train.append(traitement_images(nom_fichier3)[0])
        y_train.append([0,0,1])
    else:
        x_test.append(traitement_images(nom_fichier)[0])
        y_test.append([1,0,0])
        x_test.append(traitement_images(nom_fichier2)[0])
        y_test.append([0,1,0])
        x_test.append(traitement_images(nom_fichier3)[0])
        y_test.append([0,0,1])
    print('bmw' + str(i+1) + '/4000')
    print('mercedes' + str(i+1) + '/4000')
    print('audi' + str(i+1) + '/4000')



pool = multiprocessing.Pool(processes=cpu)
[pool.apply_async(creation_jeux, args=(i, )) for i in range(4000)]
pool.close()
pool.join()


np.save('x_train', np.asarray(x_train))
np.save('y_train', np.asarray(y_train))
np.save('x_test', np.asarray(x_test))
np.save('y_test', np.asarray(y_test))


x_train = np.load('x_train.npy')
y_train = np.load('y_train.npy')
x_test = np.load('x_test.npy')
y_test = np.load('y_test.npy')


epochs = 25

history = model.fit(x_train, y_train, batch_size = 16, epochs = epochs, verbose = 1, validation_data =(x_test, y_test))
model.save("miniprojet_n_classes.h5")



#Traçage des courbes
import matplotlib.pyplot as plt
xvals = range (epochs)
plt.clf() #Clear figure

#Plot both training and validation accuracy on the same figure
plt.plot(xvals, history.history["accuracy"], label = "Training accuracy")
plt.plot(xvals, history.history["val_accuracy"], label = "Validation accuracy")
plt.legend() #Display legend

plt.show() #Show the figure


print('END')
