import numpy as np
import csv
import itertools

# data: a csv-file
# skills: a list of the required skills in a project group
def projectGroups(data, skills):
    candidates = []
    combinations = []
    goodCombinations = []
    
    employees = {}
    with open(data, mode='r') as f:
        reader = csv.reader(f)
        employees = {rows[0]: rows[1:-1] for rows in reader}
    
    # appends candidates with any candidate with at least one relevant skill
    for i in employees:
        for j in skills:
            if j in employees[i]:
                candidates.append(i)
                break
            
    # appends combinations with all possible project groups of members with relevant skills
    for i in range(1, len(candidates) + 1):
        combinations.append(list(itertools.combinations(candidates, i)))
    
    # checks if each project group has all desired skills combined
    for i in combinations:
        for j in i:
            combinedSkills = []
            for k in j:
                combinedSkills.extend(list(employees[k]))
               
            # if a project group has all the desired skills they're appended to goodCombinations   
            if all(x in combinedSkills for x in skills):
                goodCombinations.append(j)
                
    return goodCombinations      
 

def optimizedProjectGroups(data, skills):
    goodGroups = projectGroups(data, skills)

    i = 0
    while True:
        j = i + 1
        while True:
            if j >= len(goodGroups):
                break
            elif set(goodGroups[i]).issubset(goodGroups[j]):
                goodGroups.remove(goodGroups[j])
            else:
                j += 1
        if i >= len(goodGroups) - 1:
            break
        else:
            i += 1
                
    return goodGroups

# ----main----
 
# Test matching handout example
skills = np.array(['a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't']) 
               
goodGroups = optimizedProjectGroups('emp_skills.csv', skills)

# prettyfication
print('Desired skills:',)

string = ""
for i in skills:
    string += i + " "
print(string + '\n')
    
print('Possible groups:')

for i in goodGroups:
    string = ""
    for j in i:
        string += j[0] + " "
    print(string)