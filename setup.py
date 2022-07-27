# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 12:11:34 2022

@author: prash
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import sys
import glob
import os

from setuptools import Extension

def glob_data_files(data_package, data_type=None):
    data_type = '*' if data_type is None else data_type
    data_dir = data_package.replace(".", "/")
    data_files = [] 
    directories = glob.glob(data_dir+'/**/', recursive=True) 
    for directory in directories:
        subdir = directory[len(data_dir)+1:]
        if subdir != "":
            files = subdir + data_type
            data_files.append(files)
    return data_files


here = path.abspath(path.dirname(__file__))

requires_list = []
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    for line in f:
        requires_list.append(str(line))

extras = {
}

all_deps = []
for group_name in extras:
    if group_name not in ['mujoco', 'plots']:
        all_deps += extras[group_name]
extras['all'] = all_deps

long_description = 'RLSched is a Python Reinforcement Learning (RL) library' \
                   ' whose modularity allows to easily use well-known Python' \
                   ' libraries for tensor computation (e.g. PyTorch, Tensorflow)' \
                   ' and RL benchmarks (e.g. OpenAI Gym, PyBullet, Deepmind' \
                   ' Control Suite). It allows to perform RL experiments in a' \
                   ' simple way providing classical RL algorithms to be run on scheduling simulations' \
                   ' (e.g. Q-Learning, SARSA, FQI), and deep RL algorithms' \
                   ' (e.g. DQN, DDPG, SAC, TD3, TRPO, PPO).' \


#ext_modules = [Extension('cqgym.environments.mujoco_envs.humanoid_gait.'
#                         '_external_simulation.muscle_simulation_stepupdate',
#                        ['cqgym/environments/mujoco_envs/humanoid_gait/'
#                         '_external_simulation/muscle_simulation_stepupdate.pyx'],
#                         include_dirs=[numpy.get_include()])]

#mujoco_data_package = 'cqgym.environments.mujoco_envs.data'
#pybullet_data_package = 'cqgym.environments.pybullet_envs.data'
#external_simulation_package = 'cqgym.environments.mujoco_envs.humanoid_gait._external_simulation'
setup(
    name='CQGym',
    version=1.0,
    description='A Python library for Reinforcement Learning experiments on scheduling',
    long_description=long_description,
    url='https://github.com/SPEAR-IIT/CQGym',
    author="Prashant Ravi",
    author_email='prashant.ravi@gmail.com',
    license='MIT',
    packages=find_packages(where="cqgym"),
    package_dir={"": "cqgym"},
    zip_safe=False,
    install_requires=requires_list,
    extras_require=extras,
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 ],
    cmdclass={'': ''},
    package_data={},
    dependency_links=[
    "https://download.pytorch.org/whl/cu115/torch_stable.html",
    "https://github.com/path/to/package-two@41b95ec#egg=package-two"
    ]
)