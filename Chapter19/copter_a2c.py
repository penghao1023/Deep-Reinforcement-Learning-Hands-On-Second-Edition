#!/usr/bin/env python3

import gym

import gym_copter

from a2c import parse_args, train

args = parse_args()

test_env = gym.make(args.env)

train(test_env, args)
