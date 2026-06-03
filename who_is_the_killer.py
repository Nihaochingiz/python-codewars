def killer(suspect_info, dead):
    for suspect, seen_list in suspect_info.items():
        counter = 0

        for dead_person in dead:
            if dead_person in seen_list:
                counter += 1
        if counter == len(dead):
            return suspect

print(killer({'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']))