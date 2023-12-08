import tensorflow as tf
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.models import Model




# inputs = Input(shape=(784,))
# x = Dense(64, activation='relu')(inputs)
# outputs = Dense(10, activation='softmax')(x)

# functional_model = Model(inputs=inputs, outputs=outputs)



def get_functional_model(lib):

    shape_x = 48
    shape_y = 48

    input_img = lib.layers.Input(shape=(shape_x, shape_y, 1), name='input_1')  # input

    layer_1 = lib.layers.Conv2D(1, (1, 1), padding='same', activation='relu', name='layer_1_1')(input_img)
    layer_1 = lib.layers.Conv2D(1, (3, 3), padding='same', activation='relu', name='layer_1_2')(layer_1)

    layer_2 = lib.layers.Conv2D(1, (1, 1), padding='same', activation='relu', name='layer_2_1')(input_img)
    layer_2 = lib.layers.Conv2D(1, (5, 5), padding='same', activation='relu', name='layer_2_2')(layer_2)

    layer_3 = lib.layers.MaxPooling2D((3, 3), strides=(1, 1), padding='same', name='layer_3_1')(input_img)
    layer_3 = lib.layers.Conv2D(1, (1, 1), padding='same', activation='relu', name='layer_3_2')(layer_3)

    input_img2 = lib.layers.Input(shape=(shape_x, shape_y, 1), name='input_2')  # input

    mid_1 = lib.layers.concatenate([layer_1, layer_2, layer_3, input_img2], axis=3, name='concat')

    flat_1 = lib.layers.Flatten(name='flatten')(mid_1)
    dense_1 = lib.layers.Dense(1, activation='relu', name='dense_1')(flat_1)
    dense_2 = lib.layers.Dense(1, activation='relu', name='dense_2')(dense_1)
    dense_3 = lib.layers.Dense(1, activation='relu', name='dense_3')(dense_2)
    output = lib.layers.Dense(1, activation='softmax', name='dense_4')(dense_3)

    model = lib.Model([input_img, input_img2], [output, mid_1])
    return model

functional_model = get_functional_model(tf.keras)

functional_model.save('functional_model3')