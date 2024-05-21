import json
c1 = '├' 
c2 = '─' 
c3 = '└'
c4 = '│'
c5 = '\xa0'
with open('out.txt', 'r') as f:
    data = f.read()
    data = data.replace(c1,"")
    data = data.replace(c2,"")
    data = data.replace(c3,"")
    data = data.replace(c4,"")
    data = data.replace(c5,"")
    data = data.replace(" ","")
    data = data.split('\n')
    data.remove("gitFontMap.json")
    data.remove("out.txt")
    data.remove("README.md")
    

    memory = {}
    cursor = None
    for i in data:
        if i.endswith('.ttf') or i.endswith('.otf'):
            memory[cursor].append(i)
        else:
            cursor = i
            memory[cursor] = []
    converted = json.dumps(memory, indent=2)
    with open('gitFontMap.json','w') as jfile:
        jfile.write(converted)