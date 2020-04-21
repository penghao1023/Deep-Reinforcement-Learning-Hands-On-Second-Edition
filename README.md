# Deep-Reinforcement-Learning-Hands-On-Second-Edition
Deep-Reinforcement-Learning-Hands-On-Second-Edition, published by Packt

Modified by Simon D. Levy:

1. Made a proper Python package (currently Chapter 19 only)

2. Removed RoboSchool dependency.

3. Support one-dimensional action space.

## Quickstart

```
% cd drlho2e/ch19
% python3 trpo.py -e Pendulum-v0 -n pendulum
```

After a hundred thousand iterations or so, the program should should report
saving the current best agent to a file. After a few hundred thousand iterations, the
best agent should be good enough to test, which you can do as follows:

```
% python3 play.py --render -e Pendulum-v0 -m saves/trpo-pendulum/best_-<REWARD>_<ITER>.dat
```

where ```<REWARD>``` is the amount of reward and ```<ITER>``` is the number of iterations
at which it was saved. (It is easiest to do this through tab completion.) You
should see brief animation of the pendulum rising to an upright position, indicating success.

## Installing as a Python package

To work with your own Gym environment (like [this one](https://github.com/simondlevy/gym-copter)), 
you'll want to install this repository as a Python package.  Back in the top-level directory:

```
% python3 setup.py install
```

On Linux and OS X, you'll like have to do this with <tt>sudo</tt>:

```
% sudo python3 setup.py install
```


