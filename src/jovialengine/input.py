import pygame

from . import config

import constants


class Action(object):
    __slots__ = (
        'player_id',
        'action_id',
        'action_value',
        'type',
        '__dict__',
    )

    def __init__(self, player_id: int, action_id: int, action_value: float | int, event: pygame.event.Event):
        self.player_id = player_id
        self.action_id = action_id
        self.action_value = action_value
        self.type = event.type
        self.__dict__ = event.__dict__


class Input(object):
    __slots__ = (
        'controller_states',
    )

    def __init__(self, max_players: int, num_inputs: int):
        # load in input mapping from config
        # make objects to hold onto current virtual gamepad states
        controller_states = [[0] * num_inputs for x in range(max_players)]

    def _getAction(self, event: pygame.event.Event):
        # do actual mapping
        return Action(0, 0, 0, event)

    def map(self, event: pygame.event.Event):
        action = self._getAction(event)
        self.controller_states[action.player_id][action.action_id] = action.action_value
        return action
