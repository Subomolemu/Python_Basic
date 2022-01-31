import random


class KillError(BaseException):
    def __str__(self):
        return 'KillError'


class DrunkError(BaseException):
    def __str__(self):
        return 'DrunkError'


class CarCrashError(BaseException):
    def __str__(self):
        return 'CarCrashError'


class GluttonyError(BaseException):
    def __str__(self):
        return 'GluttonyError'


class DepressionError(BaseException):
    def __str__(self):
        return 'DepressionError'


class Life:
    charm = 0
    count = 0
    
    def __init__(self, day):
        self.day = day
    
    def one_day(self):
        with open('karma.log', 'w', encoding='utf-8') as karma:
            while self.charm < 500:
                self.day += 1
                try:
                    check = random.randint(1, 10)
                    today_charm = random.randint(1, 7)
                    self.charm += today_charm
                    if check == 10:
                        error = random.randint(1, 5)
                        self.count += 1
                        
                        if error == 1:
                            raise KillError
                        elif error == 2:
                            raise DrunkError
                        elif error == 3:
                            raise CarCrashError
                        elif error == 4:
                            raise GluttonyError
                        elif error == 5:
                            raise DepressionError
                    
                except (KillError, DrunkError, CarCrashError,
                        GluttonyError, DepressionError) as caught_error:
                    karma.write(f'{self.count}. {self.day} день: '
                                f'{caught_error}\n')
  
    def __str__(self):
        return f'500 кармы набрано на {self.day} день жизни.'
       
        
start = Life(0)
start.one_day()
print(start)
