import os

class Student:
    def __init__(self, name):
        self.name=name
        self.scores=[]

    def take_exam(self, score):
        self.scores.append(score)

    def get_score_average(self):
        if len(self.scores) == 0:
            return -1
        else:
            return int(sum(self.scores) / len(self.scores))

    def get_grade(self):
        avg = self.get_score_average()
        match avg:
            case _ if avg < 0:
                return 'N/A'
            case _ if avg >= 90:
                return 'A'
            case _ if avg >= 80:
                return 'B'
            case _ if avg >= 70:
                return 'C'
            case _ if avg >= 60:
                return 'D'
            case _ if avg < 60:
                return 'F'

    def __str__(self):
         return self.name + " : " + self.get_grade()

class Graduate(Student):
    def __init__(self, name):
        super().__init__(name)

    def get_score_average(self):
        if len(self.scores) == 0:
                return -1
        elif len(self.scores) == 1:
                return self.scores[0]
        else:
              self.min_score = min(self.scores)
              self.scores.remove(self.min_score)
              return  int(sum(self.scores) / len(self.scores))

    def get_grade(self):
        avg = self.get_score_average()
        match avg:
            case _ if avg < 0:
                return 'N/A'
            case _ if avg >= 60:
                return 'P'
            case _ if avg < 60:
                return 'F'

if __name__ == '__main__':
    john = Student('John')
    john.take_exam(100)
    john.take_exam(62)
    john.take_exam(5)
    print(john.get_score_average())
    print(john.get_grade())
    print(john)
    
    jack = Graduate('Jack')
    jack.take_exam(100)
    jack.take_exam(62)
    jack.take_exam(5)
    print(jack.get_score_average())
    print(jack.get_grade())
    print(jack)
