""" This file defines the base class for the policy. """
import abc


class Policy(object):
    """ Computes actions from states/observations. """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def act(self, x, obs, t, noise):
        """
        Args:
            x: State vector.
            obs: Observation vector.
            t: Time step.
            noise: A dU-dimensional noise vector.
        Returns:
            A dU dimensional action vector.
        """
        raise NotImplementedError("Must be implemented in subclass.")