import tensorflow as tf
from keras import layers, models, callbacks, applications, optimizers, regularizers

# --- Configuración ---
IMG_SIZE = 224
BATCH_SIZE = 16
EPOCHS = 20
INIT_LR = 1e-4
WEIGHT_DECAY = 1e-4

emotion_labels = ['angry', 'disgust', 'happy', 'natural', 'sad', 'surprise']


def augment_image(image, label):
    image = tf.image.random_flip_left_right(image)
    image = tf.image.random_brightness(image, 0.08)
    return image, label


def load_dataset(filename, batch_size=BATCH_SIZE, augment=False):
    def parse_tfrecord(example):
        feature_description = {
            "image/encoded": tf.io.FixedLenFeature([], tf.string),
            "image/object/class/label": tf.io.VarLenFeature(tf.int64),
        }
        example = tf.io.parse_single_example(example, feature_description)
        image = tf.image.decode_jpeg(example["image/encoded"], channels=3)
        image = tf.image.resize(image, [IMG_SIZE, IMG_SIZE])
        image = tf.cast(image, tf.float32) / 255.0
        image = (image - [0.485, 0.456, 0.406]) / [0.229, 0.224, 0.225]

        labels_sparse = tf.sparse.to_dense(example["image/object/class/label"])
        label = tf.cond(tf.shape(labels_sparse)[0] > 0,
                       lambda: labels_sparse[0] - 1,  # 0..5
                       lambda: tf.constant(-1, dtype=tf.int64))
        return image, label

    dataset = tf.data.TFRecordDataset(filename)
    dataset = dataset.map(parse_tfrecord, num_parallel_calls=tf.data.AUTOTUNE)
    dataset = dataset.filter(lambda _, label: label >= 0)
    if augment:
        dataset = dataset.map(augment_image, num_parallel_calls=tf.data.AUTOTUNE)
    return dataset.shuffle(1000).batch(batch_size).prefetch(tf.data.AUTOTUNE)


train_ds = load_dataset("dataset1/train/Expression.tfrecord", augment=True)
val_ds = load_dataset("dataset1/valid/Expression.tfrecord")


base_model = applications.MobileNetV2(
    input_shape=(IMG_SIZE, IMG_SIZE, 3),
    include_top=False,
    weights='imagenet',
    alpha=0.5
)
base_model.trainable = True  


inputs = layers.Input(shape=(IMG_SIZE, IMG_SIZE, 3))
x = base_model(inputs, training=True)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dense(192, activation='relu', kernel_regularizer=regularizers.l2(WEIGHT_DECAY))(x)
x = layers.Dropout(0.4)(x)
outputs = layers.Dense(6, activation='softmax')(x)
model = models.Model(inputs, outputs)

model.compile(
    optimizer=optimizers.Adam(INIT_LR),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)
model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=EPOCHS,
    callbacks=[callbacks.EarlyStopping(patience=5, restore_best_weights=True)]
)

model.save('final_model.keras')
