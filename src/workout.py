""""
This module contains the Class Workout and subclasses for different types of exercises (Running, Cycling, Strength, Swimming, Skiing, Walking, Climbing, Other). Each object has attributes for calories used, date of the exercise, distance covered (if applicable to the type of workout), duration and personal rating of the workout. The methods allow to retrieve each individual attribute of the Workout object.
"""

from abc import ABC
import numpy as np
import calories, date, distance, duration, rating

class Workout(ABC):
    """
    Abstract base class for a workout.

    Attributes:
        calories (Calories): Calories burnt during workout.
        date (Date): Date of the workout.
        distance (Distance): Distance covered during the workout.
        duration (Duration): The duration of the workout.
        rating (Rating): Rating of how the workout felt.
    """
    def __init__(self, calories: calories.Calories, date: date.Date, distance: distance.Distance, duration: duration.Duration, rating: rating.Rating):
        self.calories = calories
        self.date = date
        self.distance = distance
        self.duration = duration
        self.rating = rating

    def get_calories(self):
        """
        Return the attribute of calories
        """
        return self.calories

    def get_date(self):
        """
        Return the attribute of date
        """
        return self.date

    def get_distance(self):
        """
        Return the attribute of distance
        """
        return self.distance

    def get_duration(self):
        """
        Return the attribute of duration
        """
        return self.duration

    def get_rating(self):
        """
        Return the attribute of rating
        """
        return self.rating

    def subclass_name(self):
        """
        Returns the name of the subclass (type of workout).
        """
        return self.__class__.__name__


class Running(Workout):
    """
    A running workout. See Workout for attributes.
    """
    pass

class Cycling(Workout):
    """
    A cycling workout. See Workout for attributes.
    """
    pass

class Strength(Workout):
    """
    A strength workout. See Workout for attributes.
    Distance is set to None for this type of Workout.
    """
    def __init__(self, calories: calories.Calories, date: date.Date, duration: duration.Duration, rating: rating.Rating):
        super().__init__(calories, date, np.NaN, duration, rating)

class Swimming(Workout):
    """
    A swimming workout. See Workout for attributes.
    """
    pass

class Skiing(Workout):
    """
    A skiing workout. See Workout for attributes.
    """
    pass
class Walking(Workout):
    """
    A walking workout. See Workout for attributes.
    """
    pass
class Climbing(Workout):
    """
    A climbing workout. See Workout for attributes.
    Distance is set to None in this type of Workout.
    """
    def __init__(self, calories: calories.Calories, date: date.Date,  duration: duration.Duration, rating: rating.Rating):
        super().__init__(calories, date, np.NaN, duration, rating)

class Other(Workout):
    """
    A workout that is not running, cycling, strenght, swimming, skiing, walking or climbing. 
    See Workout for attributes.
    """
    pass