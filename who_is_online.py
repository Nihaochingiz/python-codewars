# https://www.codewars.com/kata/5b6375f707a2664ada00002a/train/python
def who_is_online(friends):
    if len(friends) == 0:
        return {}

    result = {}
    for friend in friends:
            status = friend['status']

            if status == 'online' and friend['last_activity'] > 10:
                status = 'away'
            if status not in result:
                result[status] = [friend['username']]
            else:
                result[status].append(friend['username'])


    return result


print(who_is_online([
    {'username': 'David', 'status': 'online', 'last_activity': 10},
    {'username': 'Lucy', 'status': 'offline', 'last_activity': 22},
    {'username': 'Bob', 'status': 'online', 'last_activity': 104}
]))


# {
#   online: ['David'],
#   offline: ['Lucy'],
#   away: ['Bob']
# }