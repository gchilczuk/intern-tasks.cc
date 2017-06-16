from task1 import group_by
from task2 import damage


def group_by_test():
    file = open('launchlog.txt')
    print(group_by(file, 'month', success=False))  # in the instruction out wasn't filtered
    file = open('launchlog.txt')
    print(group_by(file, 'year'))


def damahe_test():
    print(damage('xxxxxfejejeeaindaiyaiaixxxxxx') == 17)
    print(damage('feeai') == 2)
    print(damage('feaineain') == 7)
    print(damage('jee') == 0)
    print(damage('fefefefefeaiaiaiaiai') == 0)
    print(damage('fdafafeajain') == 1)
    print(damage('fexxxxxxxxxxai') == 0)
    print(damage('fejejeeaindaineai') == 18)

if __name__ == '__main__':
    group_by_test()
    damahe_test()
