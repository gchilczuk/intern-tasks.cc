SUBSPELLS = {'fe' : 1,
             'je' : 2,
             'jee': 3,
             'ain': 3,
             'dai': 5,
             'ne' : 2,
             'ai' : 2,
             '-' : -1}


def damage(spell):
    start = spell.find('fe')
    end = spell.rfind('ai') + 2
    spell = spell[start:end]

    spell_is_correct = start >=0 and end >= 0
    founded_subspells = []

    print(spell)
    curr_subspell = spell[0]
    for i in range(1,len(spell)):
        pass


def evaluate_subspells(list_of_subspells):
    return sum(map(lambda sub: SUBSPELLS[sub], list_of_subspells))


