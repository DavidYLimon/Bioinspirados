import tensorflow as tf
import matplotlib.pyplot as plt

# Datos de entrenamiento
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# Preprocesar los datos
x_train = x_train / 255.0
x_test = x_test / 255.0

# Capaz de la red
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilar
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenar 
model.fit(x_train, y_train, epochs=10)

    # Evaluar la red neuronal
def evaluate_and_print_predictions():
    y_pred = model.predict(x_test)
    # Imprimir las predicciones
    n_predictions = int(input("¿Cuántas predicciones desea imprimir?"))
    fig, axes = plt.subplots(nrows=1, ncols=n_predictions)
    for i in range(n_predictions):
        axes[i].imshow(x_test[i])
        axes[i].set_title(f"Predicción    : {y_pred[i].argmax()}")
    plt.show()

evaluate_and_print_predictions()

