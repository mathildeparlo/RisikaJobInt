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
    for idx in range(1, len(candidates) + 1):
        combinations.append(
            list(itertools.combinations(candidates, idx))
        )
    
    # makes sure that each proj. group has all desired skills combined
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
    for groups_idx in range(len(good_groups)):
        count = 0
        for subgroup_idx in range(groups_idx + 1, len(good_groups)):
            subgroup_idx -= count
            if subgroup_idx >= len(good_groups):
                break
            
            elif set(good_groups[groups_idx]).issubset(
                    good_groups[subgroup_idx]):
                
                good_groups.remove(good_groups[subgroup_idx])
                count += 1
                
        if groups_idx >= len(good_groups) - 1:
            break
                
    return good_groups

# ----main----
 
# Test matching handout example
skills = (['a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't']) 
               
good_groups = optimized_project_groups('emp_skills.csv', skills)

# prettyfication
print('Desired skills:')
print(" ".join(skills))
print('Possible groups:')

for group in good_groups:
    print(" ".join(group))
