import random


class Competition:
    def __init__(self, name, points):
        self.name = name
        self.points = points


class Pupil:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.competitions = []

    def make_competitions(self):
        competitions_arr = ['run', 'jump', 'swim', 'throw', 'kick']

        for competition in competitions_arr:
            points = random.randint(0, 10)
            new_competition = Competition(competition, points)
            self.competitions.append(new_competition)

    def show_competition_points(self):
        points_sum = 0
        for competition in self.competitions:
            points_sum += competition.points
        result = {'name': self.name, 'points': points_sum}
        return result


def main():
    button = ''
    competition_points = []
    while button != 'o':
        name, surname, age = input(
            "insert name , surname and age please: ").split()
        new_pupil = Pupil(name, surname, age)
        new_pupil.make_competitions()
        pupil_result = new_pupil.show_competition_points
        competition_points.append(pupil_result)
        button = str(input('type o if u want to end else press any button: '))

    return competition_points


print(main())
