import csv
import itertools

# data: a csv-file
# desired_skills: a list of the required skills in a project group
def project_groups(data, desired_skills):
    candidates = [] # a list of employees with 1+ relevant skill
    
     # a list of lists with all project group consisting of good 
     # candidates.
     # NOTE The combination of candidates might not be good!
    combinations = []
    good_combinations = []
    
    # Turns the data into a dictionary
    employees = {}
    with open(data, mode='r') as f:
        reader = csv.reader(f)
        employees = {rows[0]: rows[1:-1] for rows in reader}
    
    # appends candidates with any candidate with 1 + relevant skills
    for employee in employees:
        for skill in desired_skills:
            if skill in employees[employee]:
                candidates.append(employee)
                break
            
    # appends combinations with lists of all possible project groups of
    # members with at least one relevant skills
    for i in range(1, len(candidates) + 1):
        combinations.append(
            list(itertools.combinations(candidates, i))
        )
    
    # makes sure that each proj. group has all desired skills combined
    for combination_list in combinations:
        for project_group in combination_list:
            combined_skills = [skill for employee in project_group for
                               skill in employees[employee]]
            
            # if a project group has all the desired skills
            # they're appended to goodCombinations   
            if all(skill in combined_skills for skill in desired_skills):
                good_combinations.append(project_group)
                
    return good_combinations      
 

def optimized_project_groups(data, skills):
    good_groups = project_groups(data, skills)

    # This is the alternative version pr request
    # To my knowledge a while loop would still be better
    
    # good_groups is ordered from smallest to biggest group.
    # Therefore we only check if a lower index group is a subset of a
    # higher index group. If it's a subset the bigger group is removed.
    for groups_idx in range(len(good_groups)):
        count = 0
        for bigger_groups_idx in range(groups_idx + 1, len(good_groups)):
            bigger_groups_idx -= count
            if bigger_groups_idx >= len(good_groups):
                break
            
            elif set(good_groups[groups_idx]).issubset(
                    good_groups[bigger_groups_idx]):
                
                good_groups.remove(good_groups[bigger_groups_idx])
                count += 1
                
        if groups_idx >= len(good_groups) - 1:
            break
                
    return good_groups

# ----main----
 
# Test matching handout example
desired_skills = (['a', 'b', 'd', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't']) 
               
good_groups = optimized_project_groups('emp_skills.csv', desired_skills)

# prettyfication
print('Desired skills:')
print(" ".join(desired_skills))
print('Possible groups:')

for idx in good_groups:
    print(" ".join(idx))
