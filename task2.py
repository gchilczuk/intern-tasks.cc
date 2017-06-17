SUBSPELLS = {'fe': 1,
             'je': 2,
             'jee': 3,
             'ain': 3,
             'dai': 5,
             'ne': 2,
             'ai': 2}
POSSIBLE_PAIRS = {'fe', 'je', 'ee', 'ai', 'in', 'da', 'ne'}


def damage(spell):
    start = spell.find('fe')
    end = spell.rfind('ai') + 2
    spell = spell[start:end]

    spell_is_correct = 0 <= start < end and len(spell) > 0

    if spell_is_correct:
        founded_subspells = [spell[:2], spell[-2:]]
        spell = spell[2:-2]

        if spell.find('fe') > -1:
            spell_is_correct = False
        else:
            creation = ''
            while len(spell) > 2:
                creation += spell[0]
                spell = spell[1:]
                maybe = creation[-1]+spell[0]
                if maybe not in POSSIBLE_PAIRS:
                    if len(creation) > 2:
                        founded_subspells += split_max_damage_subspells(creation)
                    else:
                        founded_subspells += split_smallest_subspells(creation)
                    creation = ''
            creation += spell
            if len(creation) > 2:
                founded_subspells += split_max_damage_subspells(creation)
            else:
                founded_subspells += split_smallest_subspells(creation)
        evaluated_damage = evaluate_subspells(founded_subspells)
        return evaluated_damage if spell_is_correct and evaluated_damage > 0 else 0

    return 0


def evaluate_subspells(list_of_subspells):
    return sum(map(lambda sub: SUBSPELLS.get(sub, -1*len(sub)), list_of_subspells))


def split_max_damage_subspells(string):
    small = split_smallest_subspells(string)
    big = split_biggest_subspells(string)
    return small if evaluate_subspells(small) > evaluate_subspells(big) else big


def split_smallest_subspells(string):
    splited = []
    while len(string) > 2:
        working = string[:2]
        if working in SUBSPELLS:
            splited.append(working)
            string = string[2:]
        else:
            working += string[2]
            if working in SUBSPELLS:
                splited.append(working)
                string = string[3:]
            else:
                splited.append(working[0])
                string = string[1:]

    splited.append(string)
    return splited


def split_biggest_subspells(string):
    splited = []
    while len(string) > 3:
        working = string[:3]
        if working in SUBSPELLS:
            splited.append(working)
            string = string[3:]
        else:
            working = working[:2]
            if working in SUBSPELLS:
                splited.append(working)
                string = string[2:]
            else:
                splited.append(working[0])
                string = string[1:]
    if string in SUBSPELLS:
        splited.append(string)
    else:
        splited += split_smallest_subspells(string)
    return splited
