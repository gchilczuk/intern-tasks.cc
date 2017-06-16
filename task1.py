from collections import Counter #, OrderedDict

def group_by(stream, field, success=None):
    next(stream)
    col_begins = next(stream)
    date_start_index = col_begins.find('#', 1)
    date_end_index = col_begins.find('#', date_start_index+1)
    succ_index = col_begins.rfind('#', 0, -2)
    founded = []

    prev_year = ''
    prev_month = ''
    prev_is_succ = None
    for line in stream:
        date = line[date_start_index:date_end_index].split()
        try:
            year = date[0]
            month = date[1]
            succ = line[succ_index]
            is_succ = succ == 'S'
            prev_year = year
            prev_month = month
            prev_is_succ = is_succ
        except IndexError:
            year = prev_year
            month = prev_month
            is_succ = prev_is_succ

        if success is None or success == is_succ:
            if field == 'year':
                founded.append(year)
            else:
                founded.append(month)



    d = dict(Counter(founded))
    return d # OrderedDict(sorted(d.items()))






