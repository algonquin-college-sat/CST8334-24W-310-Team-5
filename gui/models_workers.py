# models_workers.py
from PyQt5.QtCore import QThread, pyqtSignal
import tensorflow as tf
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier
import os
import sklearn.tree as tree


class WorkerTrainModel(QThread):
    def __init__(self, X, Y, n_units, n_epochs, lr, metrics, model_type, parent=None):
        QThread.__init__(self, parent)
        self.X = X
        self.Y = Y
        self.n_units = n_units
        self.n_epochs = n_epochs
        self.lr = lr
        self.metrics = metrics
        self.model_type = model_type

    worker_complete = pyqtSignal(dict)

    def run(self):
        if self.model_type == "Stochastic Gradient Descent":
            self.train_logistic_regression()
        elif self.model_type == "Decision Tree":
            self.train_decision_tree()
        elif self.model_type == "Random Forest":
            self.train_random_forest()
        elif self.model_type == "XGBoost":
            self.train_xgboost()
        elif self.model_type == "MLP Classifier":
            self.train_mlp_classifier()
        elif self.model_type == "AdaBoost":
            self.train_adaboost()

    def train_logistic_regression(self):
        """Trains a Logistic Regression model using TensorFlow"""

        sgd_optimizer = tf.keras.optimizers.SGD(
            learning_rate=self.lr, momentum=0.0, nesterov=False, name="SGD"
        )
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(self.n_units,)))
        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

        model.compile(optimizer=sgd_optimizer, loss="binary_crossentropy")

        history = model.fit(self.X, self.Y, epochs=self.n_epochs, verbose=0)

        self.worker_complete.emit({"model": model})


    def train_decision_tree(self):
        """
        Trains a Decision Tree model using scikit-learn on the dataset represented by self.X and self.Y.
        Once training is complete, it emits a signal with the trained model.
        """
        # Initialize the Decision Tree Classifier
        # You can adjust the parameters of DecisionTreeClassifier() as needed, e.g., max_depth, min_samples_split, etc.
        model = tree.DecisionTreeClassifier()

        # Train the model on the provided dataset
        # self.X represents the features and self.Y represents the target variable
        model.fit(self.X, self.Y)

        # Emit a signal upon completion with the trained model
        # This assumes you have a signal named worker_complete set up to handle post-training tasks
        self.worker_complete.emit({"model": model})

    def train_random_forest(self):
        """Used the code for default ML model; It needs to be replaced with the trained Random Forest model using scikit-learn"""

        sgd_optimizer = tf.keras.optimizers.SGD(
            learning_rate=self.lr, momentum=0.0, nesterov=False, name="SGD"
        )
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(self.n_units,)))
        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

        model.compile(optimizer=sgd_optimizer, loss="binary_crossentropy")

        history = model.fit(self.X, self.Y, epochs=self.n_epochs, verbose=0)

        self.worker_complete.emit({"model": model})

    def train_xgboost(self):
        """Used the code for default ML model; It needs to be replaced with the trained XGBoost model using scikit-learn"""

        sgd_optimizer = tf.keras.optimizers.SGD(
            learning_rate=self.lr, momentum=0.0, nesterov=False, name="SGD"
        )
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(self.n_units,)))
        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

        model.compile(optimizer=sgd_optimizer, loss="binary_crossentropy")

        history = model.fit(self.X, self.Y, epochs=self.n_epochs, verbose=0)

        self.worker_complete.emit({"model": model})

    def train_mlp_classifier(self):
        """Used the code for default ML model; It needs to be replaced with the trained MLP Classifier model using TensorFlow"""

        sgd_optimizer = tf.keras.optimizers.SGD(
            learning_rate=self.lr, momentum=0.0, nesterov=False, name="SGD"
        )
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(self.n_units,)))
        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

        model.compile(optimizer=sgd_optimizer, loss="binary_crossentropy")
        
        # Output layer
        model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

        model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=self.lr),
                      loss='binary_crossentropy',
                      metrics=self.metrics)

        history = model.fit(self.X, self.Y, epochs=self.n_epochs, verbose=0)

        self.worker_complete.emit({"model": model})

    def train_adaboost(self):
        """Used the code for default ML model; It needs to be replaced with the trained ADABoost model using scikit-learn"""

        sgd_optimizer = tf.keras.optimizers.SGD(
            learning_rate=self.lr, momentum=0.0, nesterov=False, name="SGD"
        )
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.InputLayer(input_shape=(self.n_units,)))
        model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

        model.compile(optimizer=sgd_optimizer, loss="binary_crossentropy")

        history = model.fit(self.X, self.Y, epochs=self.n_epochs, verbose=0)

        self.worker_complete.emit({"model": model})
