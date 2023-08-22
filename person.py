class Person:
    def __init__(self,wake_up_time,sleep,workout) -> None:
        self.wake_up_rate=self.wake_up(wake_up_time)
        self.sleep_rate=self.sleep(sleep)
        self.workout_rate=self.workout(workout)
        self.avrage_score = self.avrage_rate(self.wake_up_rate,self.sleep_rate,self.wake_up_rate)
    def __repr__(self) -> str:
        return f"avrage score is: {self.avrage_score}"
    def sleep(self,sleep: float)-> int:
        """give a rate about sleep timer
        3 is best time u slepp and 1 is worth time
        if u use worng value will raise"""
        if sleep>=21 and sleep < 22:
            return 3
        elif sleep >= 22 and sleep <= 24:
            return 2
        elif sleep > 1 :
            return 1
        else:
            raise ValueError("input good value!!")
    def wake_up(self,wake_up: float)-> int:
        """catch a wake up time and return a score of wake up
        best score is 3 and worth score is 0
        if u use worng value it will raise with value eror"""
        if wake_up >= 5 and wake_up <7:
            return 3
        elif wake_up >= 7 and wake_up < 9:
            return 2
        elif wake_up >= 9 and wake_up <12:
            return 1
        elif wake_up >= 12 :
            return 0
        else:
            raise ValueError("please input good value!!")
    def workout(self,workout: float)->int:
        """catch number of how many u work out per day
        3 is best number of score 0 is worth number score
        and return a integer number """
        if workout > 2 :
            return 3
        elif workout <= 2 and workout > 1 :
            return 2
        elif workout <= 1 and workout > 0:
            return 1
        elif workout <= 0 :
            return 0
        else:
            raise ValueError("u use worng value!!")
    def avrage_rate(self,wake_up_rate,sleep_rate,workout_rate)-> float:
        """catch avrage of score per day
        its mean catch evry of score and give one avrage score in day
        3 is best number and 0 is worth number"""
        score = (wake_up_rate+sleep_rate+workout_rate)/3
        return score
parsa=Person(5,21,3)
print(parsa)