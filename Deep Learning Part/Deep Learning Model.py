


import pandas as pd
import os, glob
import numpy as np
import datetime, os
from keras.callbacks import TensorBoard
import tensorflow as tf



In1 = f'.csv'
In2 = f'.csv'


print("*** Merging multiple csv files into a single pandas dataframe ***")

# merge files
dataFrameInput = pd.concat(
   map(pd.read_csv, [In1,In2]), ignore_index=True)
print(dataFrameInput)


Out1 = f'.csv'
Out2 = f'.csv'


print("*** Merging multiple csv files into a single pandas dataframe ***")

# merge files
dataFrameOut = pd.concat(
   map(pd.read_csv, [Out1, Out2]), ignore_index=True)
print(dataFrameOut)


if len(dataFrameInput) == len(dataFrameOut):
    print("True")


dataFrameInput


dataFrameOut


dataFrameInput = dataFrameInput[dataFrameInput['Height'].isna() == False]
dataFrameOut = dataFrameOut[dataFrameOut['OUTR'].isna() == False]


data = pd.merge(dataFrameInput,dataFrameOut,suffixes=('_l', '_r'),left_index =True,right_index =True)


data



len(data.columns)


dataset = data.values


dataset

len(dataset)

X = dataset[:,0:81]
X

Y = dataset[:,81:84]
Y


from sklearn import preprocessing


min_max_scaler = preprocessing.MinMaxScaler()
X_scale = min_max_scaler.fit_transform(X)


X_scale


from sklearn.model_selection import train_test_split

X_train, X_val_and_test, Y_train, Y_val_and_test = train_test_split(X_scale, Y, test_size=0.3)


X_val, X_test, Y_val, Y_test = train_test_split(X_val_and_test, Y_val_and_test, test_size=0.5)


print(X_train.shape, X_val.shape, X_test.shape, Y_train.shape, Y_val.shape, Y_test.shape)


from keras.models import Sequential,load_model
from keras.layers import Dense


model = load_model('Model.HDF5')


from tensorflow import keras

model = Sequential([
    Dense(1024, activation='relu', input_shape=(81,)),
    Dense(1024, activation='relu'),
    Dense(3, activation='relu'),
])


model.compile(optimizer='adam',
              loss='mae',
              metrics=['accuracy'])


tf.keras.utils.plot_model(model, show_shapes=True, dpi=64)


hist = model.fit(X_train, Y_train,
          batch_size=128, epochs=1,
          validation_data=(X_val, Y_val), callbacks=[tensorboard_callback])


model.evaluate(X_test, Y_test)[1]


import numpy as num
import matplotlib.pyplot as plot

from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import ConfusionMatrixDisplay


iris = datasets.load_iris()
x = iris.data
y = iris.target
class_names = iris.target_names


x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)


classifier = svm.SVC(kernel="linear", C=0.02).fit(x_train, y_train)

num.set_printoptions(precision=2)

title_options = [
    ("Confusion matrix, without normalization", None),
    ("Normalized confusion matrix", "true"),
]
for title, normalize in title_options:
    display = ConfusionMatrixDisplay.from_estimator(
        classifier,
        x_test,
        y_test,
        display_labels=class_names,
        cmap=plot.cm.Blues,
        normalize=normalize,
    )
    display.ax_.set_title(title)

    print(title)
    print(display.confusion_matrix)

plot.show()



model.save("Model.HDF5")



import matplotlib.pyplot as plt


print(hist.history.keys())


# summarize history for accuracy
plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


# summarize history for loss
plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()


pred = model.predict(X_test)


ev = model.evaluate(X_test, Y_test)

len(X_test)


len(Y_test)


len(X_test[0])


Y_test[:4096]


pred[:4096]






