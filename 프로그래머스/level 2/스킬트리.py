def solution(skill, skill_trees):
    cnt = 0
    
    for i in skill_trees:
        skill_list = ''
        
        for j in i:
            if j in skill:
                skill_list += j
        
        if skill_list == skill[0:len(skill_list)]:
            cnt += 1
    
    return cnt

skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]


result = solution(skill, skill_trees)