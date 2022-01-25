import random


class KillError(BaseException):
    pass


class DrunkError(BaseException):
    pass


class CarCrashError(BaseException):
    pass


class GluttonyError(BaseException):
    pass


class DepressionError(BaseException):
    pass


class Life:
    charm = 0
    count = 0
    
    def __init__(self, day):
        self.day = day
    
    def one_day(self):
        with open('karma.log', 'w', encoding='utf-8') as karma:
            while self.charm < 500:
                self.day += 1
                check = random.randint(1, 10)
                if check == 10:
                    
                        error = random.randint(1, 5)
                        self.count += 1
                        try:
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
                        except KillError:
                            karma.write(f'{self.count}. {self.day} день: '
                                        f'{KillError}\n')
                        except DrunkError:
                            karma.write(f'{self.count}. {self.day} день:'
                                        f'{DrunkError}\n')
                        except CarCrashError:
                            karma.write(f'{self.count}. {self.day} день:'
                                        f':{CarCrashError}\n')
                        except GluttonyError:
                            karma.write(f'{self.count}. {self.day} день:'
                                        f':{GluttonyError}\n')
                        except DepressionError:
                            karma.write(f'{self.count}. {self.day} день:'
                                        f'{DepressionError}\n')
                                
                else:
                    today_charm = random.randint(1, 7)
                    self.charm += today_charm
        
    def __str__(self):
        return f'500 кармы набрано на {self.day} день жизни.'
       
        
start = Life(0)
start.one_day()
print(start)


