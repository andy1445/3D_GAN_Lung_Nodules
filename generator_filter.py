import keras
import numpy as np
import matplotlib.pyplot as plt

latent_dim = 200

#use a file to a instantiate a model for generating new training examples
def load_generator(generator_file):
    g_model = keras.models.load_model(generator_file)
    return g_model

def generate_images(generator, quantity):
    the_noise = np.random.normal(0, 1, (quantity, latent_dim))
    return generator.predict(the_noise)

def filter_images(images):
    filtered = list()
    unfiltered = list()
    for img in images:
        if np.mean(img, (1, 2, 3, 4)) > .9:
            filtered.append(img)
        else:
            unfiltered.append(img)

    return filtered, unfiltered


generator_file = 'our_models/saved_models/g1.h5'

generator = load_generator(generator_file)
fake_images = generate_images(generator, 50)
filtered, unfiltered = filter_images(fake_images)

fig, axs = plt.subplots(3, 6)

filtered_dir = 'images/filtered/'
unfiltered_dir = 'images/unfiltered/'

for img in filtered:
    for i in range(3):
        for j in range(6):
            axs[i,j].imshow(0.5 * posdat[k,:,:,cnt,0] + 0.5, cmap='gray')
            # axs[i, j].imshow(0.5 * posdat[k, :, :, cnt] + 0.5, cmap='gray')
            axs[i,j].axis('off')
            cnt += 1

    cnt = 0
    fig.savefig(filtered + 'test'+str(k)+'.png')

for img in unfiltered:
    for i in range(3):
        for j in range(6):
            axs[i, j].imshow(0.5 * posdat[k, :, :, cnt, 0] + 0.5, cmap='gray')
            # axs[i, j].imshow(0.5 * posdat[k, :, :, cnt] + 0.5, cmap='gray')
            axs[i, j].axis('off')
            cnt += 1

    cnt = 0
    fig.savefig(unfiltered + 'test' + str(k) + '.png')


