# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:59:59 2022

@author: prash
"""
from cqgym import cqsim
ver=["torch"]
alg=["PG"]
lr=0.001

class dotdict(dict):
    """dot.notation access to dictionary attributes"""
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

opts={
    'job_trace':'train.swf',
    'node_struc': 'train.swf',
    'job_save':None,
    'node_save':None,
    'cluster_fraction': None,
    'start':None,
    'start_date':None,
    'anchor':None,
    'read_num': 1500,
    'pre_name':None,
    'output':None,
    'ext_fmt_j':None,
    'ext_fmt_n':None,
    'ext_fmt_j_c':None,
    'ext_fmt_n_c':None,
    'path_in':None,
    'path_out':None,
    'path_fmt':None,
    'path_debug':None,
    'ext_jr':None,
    'ext_si':None,
    'ext_ai':None,
    'ext_ri':None,
    'ext_li':None,
    'ext_debug':None,
    'debug_lvl':0,
    'alg':None,
    'alg_sign':None,
    'backfill':3,
    'bf_para':None,
    'win':None,
    'win_para':None,
    'ad_bf':None,
    'ad_bf_para':None,
    'ad_win':None,
    'ad_win_para':None,
    'ad_alg':None,
    'ad_alg_para':None,
    'config_n':"config_n.set",
    'config_sys':"config_sys.set",
    'monitor':None,
    'log_freq':60000,
    'read_input_freq':None,
    'is_training':1,
    'rl_alg':'',
    'learning_rate':None,
    'window_size':None,
    'reward_discount':None,
    'layer_size':None,
    'batch_size':50,
    'input_weight_file':"",
    'output_weight_file': "",
    'do_render': 0
}

for v in ver:
  for a in alg:
    r = 0
    train_opts = {'job_trace': 'lublin_256.swf' , 
                  'node_save': 'lublin_256.swf',
                  'read': 1500 , 'is_training': 1 ,
                  'rl_alg': "$a", 'learning_rate': lr ,
                  'reward_discount': 0.99, 'batch_size': 50,
                  'window_size': 20, 
                  'output_weight_file': "v" + "a" +"-0",
                  'anchor': r}
    temp = train_opts.copy()
    train_opts.update(opts)
    train_opts.update(temp)
    cqsim.evaluate(dotdict(train_opts));
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
      cqsim.evaluate(dotdict(train_opts));
    for i in range(11, 20):
      o=i+1 
      r=750*i
      train_opts = {'job_trace': 'lublin_256.swf' , 
                    'node_save': 'lublin_256.swf',
                    'read': 1500 , 'is_training': 1 ,
                    'rl_alg': "$a", 'learning_rate': lr ,
                    'reward_discount': 0.99, 'batch_size': 50,
                    'window_size': 20, 
                    'output_weight_file': "v" + "a" +"-0",
                    'anchor': r}
      temp = train_opts.copy()
      train_opts.update(opts)
      train_opts.update(temp)
      cqsim.evaluate(dotdict(train_opts));
    for i in range(21, 100):  
      o=i+1 
      r=750*i
      train_opts = {'job_trace': 'lublin_256.swf' , 
                    'node_save': 'lublin_256.swf',
                    'read': 1500 , 'is_training': 1 ,
                    'rl_alg': "$a", 'learning_rate': lr ,
                    'reward_discount': 0.99, 'batch_size': 50,
                    'window_size': 20, 
                    'output_weight_file': "v" + "a" +"-0",
                    'anchor': r}
      temp = train_opts.copy()
      train_opts.update(opts)
      train_opts.update(temp)
      cqsim.evaluate(dotdict(train_opts));