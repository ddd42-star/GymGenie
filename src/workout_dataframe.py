import pandas as pd

class Workout_dataframe:
    """
    Represents a Dataframe  that contains the information from the user.

    """
    def __init__(self, exercise, date, duration, distance, calories, rating):
        self.exercise = exercise
        self.date = date
        self.duration = duration
        self.distance = distance
        self.calories = calories
        self.rating = rating
    
    def create_dataframe(self): #need to be tested, edit exercise
        """
        Create a new dataframe with the columns: 
            date
            duration
            distance
            calories
            rating

        Args:
            workout (Workout class object): Workout input from the user.
            date (datetime) : Date of the workout.
            duration (int) : Duration of the workout.
            distance (int) : Distance covered during the workout if it is evaluable in the activity perfomed.
            calories (int) : Calories burned during the workout.
            rating (int) : Represents the feeling on the workout on a scale of 1 to 10.

        """
        activity = self.exercise.subclass_name()

        dataframe = pd.DataFrame({'activity': [activity], 'date': [self.date] , 'duration (min)' : [self.duration],
                                        'distance (km)' : [self.distance], 'calories (kcal)' : [self.calories], 'rating' : [self.rating]})
        return dataframe
    
    def read_dataframe(self,dataframe):
        """
        Print the dataframe created.

        """
        print(dataframe)
    
    def edit_dataframe(self, idx, column, new_value):# it needs to be checked
        """
        Edit the information of the desired column and desired idx of the dataframe.

        Args:
            idx (int) : index that refers to the desired row to be edited.(e.g. 'duration')
            column (str): desired column to be edited.(e.g. 'duration').
            new_value (int or str) : The new value to be assigned to the specified location.
        
        """
        self.dataframe.loc[idx , column] = new_value
    
    def save_dataframe(self, path):
        """
        Save the dataframe as csv file.

        Args:
            path : path that points where to save the dataframe.
        """
        self.dataframe.to_csv(path)


#test everything
