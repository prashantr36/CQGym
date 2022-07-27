# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:59:59 2022

@author: prash
"""
import cqgym
ver=["torch"]
alg=["PG"]
lr=0.001

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


for v in ver:
  for a in alg:
    cqsim -j sample.swf -n sample.swf -R 1500 --is_training 1 --rl_alg "$a" --learning_rate $l --reward_discount 0.99 --batch_size 50 --window_size 20 --output_weight_file "$v$a-1" ;
    for i in range(1, 10):
      o=i+1 
      r=750*i
      train_opts = {'job_trace': 'lublin_256.swf' , 
                    'node_save': 'lublin_256.swf',
                    'read': 1500 , 'is_training': 1 ,
                    'rl_alg': "$a", 'learning_rate': lr ,
                    'reward_discount': 0.99, 'batch_size': 50,
                    'input_weight_file' : "v" + "a" +"-" + (i-1),
                    'window_size': 20, 
                    'output_weight_file': "v" + "a" +"-" + (i),
                    'anchor': r}
      cqsim.eval(dotdict(train_opts));
    for i in range(11, 20):
      o=i+1 
      r=750*i
      train_opts = {'job_trace': 'lublin_256.swf' , 
                    'node_save': 'lublin_256.swf',
                    'read': 1500 , 'is_training': 1 ,
                    'rl_alg': "$a", 'learning_rate': lr ,
                    'reward_discount': 0.99, 'batch_size': 50,
                    'input_weight_file' : "v" + "a" +"-" + (i-1),
                    'window_size': 20, 
                    'output_weight_file': "v" + "a" +"-" + (i),
                    'anchor': r}
      cqsim.eval(dotdict(train_opts));
    for i in range(21, 100):  
      o=i+1 
      r=750*i
      train_opts = {'job_trace': 'lublin_256.swf' , 
                    'node_save': 'lublin_256.swf',
                    'read': 1500 , 'is_training': 1 ,
                    'rl_alg': "$a", 'learning_rate': lr ,
                    'reward_discount': 0.99, 'batch_size': 50,
                    'input_weight_file' : "v" + "a" +"-" + (i-1),
                    'window_size': 20, 
                    'output_weight_file': "v" + "a" +"-" + (i),
                    'anchor': r}
      cqsim.eval(dotdict(train_opts));