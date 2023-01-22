import os
import bs4

parts = {}
cache = {}

def make_file(name, parts):
    ret = ""
    for part in parts:
        ret = ret+'\n{% include "parts/'+part+'.html" %}'
        with open("parts/"+part+".html","w") as f:
            if isinstance(parts[part], list):
                [f.write(str(x)) for x in parts[part]]
            else:
                f.write(str(parts[part]))
    with open(name, "w") as d:
        d.write(ret)

def make_cache():
    for item in cache.keys():
        data = cache[item]
        head = data.find('head')
        parts['head'] = str(head)
        
        parts['head_script'] = head.findAll('script')
        parts['head_style'] = head.findAll('style')
        
        
        body = data.find('body')
        parts['body'] = str(body)
        
        parts['body_script'] = body.findAll('script')
        parts['body_style'] = body.findAll('style')
    make_file(item, parts)

def remake_file(item):
    with open(item.path) as file:
        cache[item.name] = bs4.BeautifulSoup(file.read(), features="lxml")
    make_cache()

def remake_dir(directory):
    for item in os.scandir(directory):
        if item.is_dir():
            remake_dir(item.path)
        elif item.is_file() and item.name.endswith(".html"):
            remake_file(item)
            return

def main(template_dir, output_dir=None):
    output_dir = output_dir or template_dir+" output"
    remake_dir(template_dir)


main('./templates/dark')

print(parts)