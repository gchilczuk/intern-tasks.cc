from task1 import group_by
from task2 import damage


def group_by_test():
    file = open('launchlog.txt')
    print(group_by(file, 'month', success=False))  # in the instruction out wasn't filtered
    file = open('launchlog.txt')
    print(group_by(file, 'year'))


def damage_test():
    print(damage('xxxxxfejejeeaindaiyaiaixxxxxx') == 17)
    print(damage('feeai') == 2)
    print(damage('feaineain') == 7)
    print(damage('jee') == 0)
    print(damage('fefefefefeaiaiaiaiai') == 0)
    print(damage('fdafafeajain') == 1)
    print(damage('fexxxxxxxxxxai') == 0)
    print(damage('fejejeeaindaineai') == 18)
    print(damage('fedaineai') == 1 + 5 + 2 + 2)
    print(damage('fedaineiai') == 1 + 5 + 2 + 2 - 1)
    print(damage('feaineiai') == 1 + 2 + 2 + 2 - 1)

if __name__ == '__main__':
    group_by_test()
    damage_test()
