import random
class DailyRoutine:

    def __init__(self):
        self.current_state = "Sleep"
        self.mood = ["Bad", "Neutral", "Good"]

    def schedule(self):
        print("Day in a life:")
        for hour in range(24):
            if self.current_state == "Sleep":
                if hour in range(0, 7):
                    print(f"Time is {hour}:00.\nZzz..z..z... z\n ")
                    self.current_state = "Sleep"
                elif hour == 7:
                    mood = random.choice(self.mood)
                    if mood == "Bad":
                        print(f"Time is {hour}:00.\nNot today.\n ")
                    elif mood == "Neutral" or mood == "Good":
                        print(f"Time is {hour}:00.\nTime to get up!\n ")
                        self.current_state = "Eat"
                elif hour > 7:
                    print(f"Time is {hour}:00.\nNo time for breakfast today.\n ")
                    self.current_state = "Study"
            elif self.current_state == "Eat":
                if hour in range(0, 7):
                    print(f"Time is {hour}:00.\nMidnight snack time!\n ")
                    self.current_state = "Sleep"
                elif hour in range(7, 10):
                    breakfast = random.choice([1, 2])
                    if breakfast == 1:
                        print(f"Time is {hour}:00.\nIt is good assortment of breakfast choices in trapesna!\n ")
                        self.current_state = "Study"
                    else:
                        print(f"Time is {hour}:00.\nI would like to eat somewhere else.\n ")
                        self.current_state = "Routine"
                elif hour in range(13, 16):
                    print(f"Time is {hour}:00.\nLunch time.\n ")
                    self.current_state = "Rest"
                elif hour in range(19, 20):
                    print(f"Time is {hour}:00.\nTrapesna would be closed soon, time to have dinner!\n ")
                    self.current_state = "Study"
                elif hour >= 20:
                    print(f"Time is {hour}:00.\nTrapesna is closed now.\n ")
                    self.current_state = "Routine"
                else:
                    print("I'll eat later.\n")
                    self.current_state = "Study"
            elif self.current_state == "Study":
                if hour < 7 or hour > 22:
                    exam = random.choice([1, 2])
                    if exam == 1:
                        print(f"Time is {hour}:00.\nTime to sleep!\n ")
                        self.current_state = "Sleep"
                    else:
                        print(f"Time is {hour}:00.\nI have to study for the exams\n ")
                        self.current_state = "Study"
                else:
                    task = random.choice([1, 2, 3, 4])
                    if task == 1:
                        print(f"Time is {hour}:00.\nI have done a lot, time to have some rest!\n ")
                        self.current_state = "Rest"
                    elif task == 2:
                        print(f"Time is {hour}:00.\nI'm hungry a bit\n ")
                        self.current_state = "Eat"
                    else:
                        print(f"Time is {hour}:00.\nFew tasks left...\n ")
                        self.current_state = "Study"
            elif self.current_state == "Routine":
                if hour in range(7, 16) or hour == 22:
                    company = random.choice([1, 2])
                    if company == 1:
                        print(f"Time is {hour}:00.\nI`ll go to 'Silpo' to buy some groceries.\n ")
                        self.current_state = "Study"
                    else:
                        print(f"Time is {hour}:00.\nMy friend would keep me a company! After shopping we will hangout for a bit!\n ")
                        self.current_state = "Rest"
                if hour == 23:
                    print(f"Time is {hour}:00.\nI'm tired...\n ")
                    self.current_state = "Sleep"
                else:
                    print(f"Time is {hour}:00.\nI have to study now.\n ")
                    self.current_state = "Study"
            elif self.current_state == "Rest":
                if hour < 7 or hour > 22:
                    print(f"Time is {hour}:00.\nTime to sleep!\n ")
                    self.current_state = "Sleep"
                else:
                    mood = random.choice(self.mood)
                    if mood == "Neutral":
                        print(f"Time is {hour}:00.\nI'll watch something online.\n ")
                        self.current_state = "Study"
                    elif mood == "Good":
                        print(f"Time is {hour}:00.\nTime to go for a walk with friend!\n ")
                        self.current_state = "Study"
                    else:
                        print(f"Time is {hour}:00.\nMaybe time to have some snack?\n ")
                        self.current_state = "Eat"


day = DailyRoutine()
day.schedule()