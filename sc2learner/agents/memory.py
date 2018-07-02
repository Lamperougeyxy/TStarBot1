from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from collections import namedtuple
import random


Transition = namedtuple('Transition',
                        ('observation', 'action', 'reward', 'next_observation',
                         'done', 'mc_return'))


class ReplayMemory(object):
  def __init__(self, capacity):
    self._capacity = capacity
    self._memory = []
    self._position = 0

  def push(self, *args):
    if len(self._memory) < self._capacity:
      self._memory.append(None)
      #from copy import deepcopy
      #for i in range(self._capacity):
        #self._memory.append(deepcopy(Transition(*args)))
      #print("Replay Full.")
    self._memory[self._position] = Transition(*args)
    self._position = (self._position + 1) % self._capacity

  def sample(self, batch_size):
    return random.sample(self._memory, batch_size)

  def __len__(self):
    return len(self._memory)
