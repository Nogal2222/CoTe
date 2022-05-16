import re

def solution(word, pages):
    webpage = []
    webpage_name = []
    webpage_graph = dict()
    
    for page in pages:
        url = re.search('<meta property="og:url" content="(\S+)"', page).group(1)
        basic_score = 0
        
        for f in re.findall(r'[a-zA-Z]+', page.lower()):
            if f == word.lower():
                basic_score += 1
        
        exios_link = re.findall('<a href="(https://[\S]*)"', page)
        
        for link in exios_link:
            if link not in webpage_graph.keys():
                webpage_graph[link] = [url]
            
            else:
                webpage_graph[link].append(url)
        
        webpage_name.append(url)
        webpage.append([url, basic_score, len(exios_link)])
    
    max_value = 0
    answer = 0
    
    for i in range(len(webpage)):
        url = webpage[i][0]
        score = webpage[i][1]
        
        if url in webpage_graph.keys():
            for link in webpage_graph[url]:
                a, b, c = webpage[webpage_name.index(link)]
                score += (b / c)
        
        if max_value < score:
            max_value = score
            answer = i
    
    return answer