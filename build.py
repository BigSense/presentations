#!/usr/bin/env python3

import glob
from os import path
import sys

html_section = """
<section>{}</section>
"""

md_section = """
<section data-markdown>
  <script type="text/template">
  {}
  </script>
</section>
"""

def slide_content(slide):
  if slide.strip().endswith('set'):
    with open(path.join('sets', slide.strip()), 'r') as fd:
      return slide_file(fd)
  else:  
    with open(path.join('slides', slide.strip()),'r') as section:
      if slide.strip().endswith('html'):
        return html_section.format(section.read())
      if slide.strip().endswith('md'):
        return md_section.format(section.read())
      return 'unknown markup type'

def slide_file(fd):
  slides = fd.readlines()
  content = ''
  for slide in slides:
    if ',' in slide:
      sub_content = ''
      for sub_slide in slide.split(','):
        sub_content += slide_content(sub_slide.strip())
      content += '<section>{}</section>'.format(sub_content) 
    else:
      content += slide_content(slide)
  return content


if __name__ == '__main__':

  if len(sys.argv) > 1 and sys.argv[1] == 'clean':
    print('todo implement')
    exit(0)

  slide_files = glob.glob('*.slides')
  top = open('template/head.html', 'r').read()
  bottom = open('template/tail.html', 'r').read()

  with open('index.html','w') as index:
    with open('template/index-head.html', 'r') as itop:
      index.write(itop.read())
    with open('template/index-tail.html', 'r') as ibottom:
      index.write(ibottom.read())

    for presentation in slide_files:

      print('Processing {}'.format(presentation))
      name = presentation.split('.')[0]
      index.write('<p><a href="{}.html">{} Slides</a></p>'.format(name,name.title()))
      
      with open(presentation,'r') as fd:
        with open('{}.html'.format(name), 'w') as out:
          out.write(top)
          out.write(slide_file(fd))
          out.write(bottom)



