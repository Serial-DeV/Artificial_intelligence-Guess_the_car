import numpy as np
from PIL import Image


def traitement_images(nom_fichier):
    img = Image.open(nom_fichier) # Chargement de l'image
    img = img.resize((224, 224)) # Redimensionnement

    r, g, b = img.split() # On sépare les 3 composantes
    img = Image.merge("RGB", (b, g, r)) # On les assemble en modifiant b et r

    img = np.asarray(img, dtype = float) # Conversion de l'image en array

    # Retrait des valeurs moyennes pour les 3 composantes de chaque pixel
    for i in range(224):
        for j in range(224):
            img[i,j] = (img[i,j,0] - 103.939, img[i,j,1] - 116.779, img[i,j,2] - 123.68)

    # Modification de la structure
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    return(img)

