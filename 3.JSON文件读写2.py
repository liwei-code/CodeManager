import json

with open('test.ipynb', encoding='utf8') as fp:
    content = json.load(fp)
    
with open('program.py', 'w') as fp:
    for item in content['cells']:
        fp.writelines([i.rstrip()+'\n' for i in item['source']])