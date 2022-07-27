import numpy as np
import random
from collections import deque
import tensorflow.compat.v1 as tf
import keras.backend as K
tf.disable_v2_behavior()


class DQL:
    def __init__(self, env, sess, window_size=50, learning_rate=1e-2,
                 gamma=0.99, batch_size=20, layer_size=[]):
        self.hidden1_size = layer_size[0]
        self.hidden2_size = layer_size[1]

        self.env = env
        self.sess = sess

        self.window_size = window_size
        self.batch_size = batch_size
        self.lr = learning_rate
        self.gamma = gamma
        self.memory = deque(maxlen=20)
        self.reward_seq = []

        self.policy, self.predict = self.build_policy()

    def build_policy(self):
        obs_shape = self.env.observation_space.shape
        input = tf.keras.layers.Input(shape=obs_shape)
        input_reshape = tf.reshape(input, [-1, obs_shape[2], 1])
        conv1d = tf.keras.layers.Conv1D(1, obs_shape[2], input_shape=(obs_shape[2], 1))(input_reshape)
        conv1d_reshape = tf.reshape(conv1d, [-1, obs_shape[1]])
        hidden_layer1 = tf.keras.layers.Dense(self.hidden1_size, 'relu', input_shape=(obs_shape[1],), use_bias=False)(conv1d_reshape)
        hidden_layer2 = tf.keras.layers.Dense(self.hidden2_size, 'relu', input_shape=(self.hidden1_size,), use_bias=False)(hidden_layer1)
        output = tf.keras.layers.Dense(1, activation='sigmoid')(hidden_layer2)

        def custom_loss(y_true, y_pred):
            advantage = y_true - y_pred

            return K.sum(K.square(advantage))

        policy = tf.keras.Model(inputs=input, outputs=output)
        adam = tf.keras.optimizers.Adam(lr=self.lr)
        policy.compile(loss=custom_loss, optimizer=adam)
        predict = tf.keras.Model(inputs=[input], outputs=[output])
        return policy, predict

    def act(self, obs):
        return self.predict.predict(obs)

    def train(self):
        if len(self.memory) < self.batch_size:
            return

        states = np.zeros((self.batch_size, *self.env.observation_space.shape))
        actions = np.zeros([self.batch_size, 1])
        G = np.zeros(self.batch_size)

        for i in range(self.batch_size):
            reward_sum = 0
            discount = 1
            for j in range(i, self.batch_size):
                _, _, reward, _ = self.memory[j]
                reward_sum += reward * discount
                discount *= self.gamma
            G[i] = reward_sum

            states[i, :], actions[i, :], _, _ = self.memory[i]

        mean = np.mean(G)
        std = np.std(G) if np.std(G) > 0 else 1
        G = (G - mean) / std

        self.policy.train_on_batch([states, G], actions)
        self.memory = deque(maxlen=self.batch_size)

    def remember(self, obs, action, reward, new_obs):
        self.memory.append([obs, action, reward, new_obs])
        self.reward_seq.append(reward)

    def save(self, policy_fp, predict_fp):
        self.policy.save_weights(policy_fp)
        self.predict.save_weights(predict_fp)

    def load(self, policy_fp, predict_fp):
        self.policy.load_weights(policy_fp)
        self.predict.load_weights(predict_fp)

    def save_using_model_name(self, model_name_path):
        self.save(model_name_path + "_policy_.h5", model_name_path + "_predict_.h5")

    def load_using_model_name(self, model_name_path):
        self.load(model_name_path + "_policy_.h5", model_name_path + "_predict_.h5")
