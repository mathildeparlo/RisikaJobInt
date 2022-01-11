import csv
import itertools

# data: a csv-file
# skills: a list of the required skills in a project group
def project_groups(data, skills):
    candidates = [] # a list of employees with 1+ relevant skill
    combinations = [] # a list of lists with possible project group
    good_combinations = []
    
    employees = {}
    with open(data, mode='r') as f:
        reader = csv.reader(f)
        employees = {rows[0]: rows[1:-1] for rows in reader}
    
    # appends candidates with any candidate with 1 + relevant skill
    for employee in employees:
        for skill in skills:
            if skill in employees[employee]:
                candidates.append(employee)
                break
            
    # appends combinations with lists of all possible project groups of
    # members with at least one relevant skills
    for i in range(1, len(candidates) + 1):
        combinations.append(
                    list(itertools.combinations(candidates, i))
                    )
    
    # makes sure that each project group has all desired skills combined
    for combination_list in combinations:
        for project_group in combination_list:
            combined_skills = [skill for employee in project_group for
                               skill in employees[employee]]
            
            # if a project group has all the desired skills
            # they're appended to goodCombinations   
            if all(skill in combined_skills for skill in skills):
                good_combinations.append(project_group)
                
    return good_combinations      
 

def optimized_project_groups(data, skills):
    good_groups = project_groups(data, skills)

    # This is the alternative version pr request
    # To my knowledge a while loop would still be better
    for i in range(len(good_groups)):
        count = 0
        for j in range(i + 1, len(good_groups)):
            j -= count
            if j >= len(good_groups):
                break
            
            elif set(good_groups[i]).issubset(good_groups[j]):
                good_groups.remove(good_groups[j])
                count += 1
                
        if i >= len(good_groups) - 1:
            break
                
    return good_groups

# ----main----
 
# Test matching handout example
skills = (['a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't']) 
               
good_groups = optimized_project_groups('emp_skills_letters.csv', skills)

# prettyfication
print('Desired skills:')
print(" ".join(skills))
print('Possible groups:')

for i in good_groups:
    print(" ".join(i))
