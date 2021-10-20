from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img


datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.2,
        zoom_range=0.2,
        brightness_range = [0.7,1.3],
        horizontal_flip=True,
        fill_mode='nearest')

import multiprocessing
nb_cores = 8

def func(n,):
    img = load_img('./original/Mercedes/mercedes' + str(n+1) +'.jpg')  # this is a PIL image
    img2 = load_img('./original/BMW/bmw' + str(n+1) +'.jpg')
    img3 = load_img('./original/Audi/audi' + str(n+1) +'.jpg')
    
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x2 = img_to_array(img2)
    x3 = img_to_array(img3)
    
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)
    x2 = x2.reshape((1,) + x2.shape)
    x3 = x3.reshape((1,) + x3.shape)
    
    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='./generated/Mercedes', save_prefix='mercedes' + str(n), save_format='jpg'):
        i += 1
        if i >= 20:
            break  # otherwise the generator would loop indefinitely
    i = 0     
    for batch in datagen.flow(x2, batch_size=1,
                              save_to_dir='./generated/BMW', save_prefix='bmw' + str(n), save_format='jpg'):
        i += 1
        if i >= 20:
            break  # otherwise the generator would loop indefinitely
    i = 0
    for batch in datagen.flow(x3, batch_size=1,
                              save_to_dir='./generated/Audi', save_prefix='audi' + str(n), save_format='jpg'):
        i += 1
        if i >= 20:
            break  # otherwise the generator would loop indefinitely
  

pool = multiprocessing.Pool(processes=nb_cores)
[pool.apply_async(func, args=(n, )) for n in range(200)]
pool.close()
pool.join()

