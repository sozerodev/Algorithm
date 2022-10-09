import collections


def solution(participant, completion):

    result = collections.defaultdict(int)
    for person in participant:
        result[person] -= 1
    
    for person in completion:
        result[person] += 1
    
    for i in result:
        if result[i] < 0:
            return i