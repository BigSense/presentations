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
  with open(path.join('slides', slide.strip()),'r') as section:
    if slide.strip().endswith('html'):
      return html_section.format(section.read())
    if slide.strip().endswith('md'):
      return md_section.format(section.read())
    return 'unknown markup type'

if __name__ == '__main__':

  if len(sys.argv) > 0 and sys.argv[1] == 'clean':
    print('todo implement')
    exit(0)

  slide_files = glob.glob('*.slides')
  top = open('template/head.html', 'r').read()
  bottom = open('template/tail.html', 'r').read()

  for presentation in slide_files:
    print('Processing {}'.format(presentation))
    with open(presentation,'r') as fd:
      with open('{}.html'.format(presentation.split('.')[0]), 'w') as out:
        out.write(top)
        slides = fd.readlines()
        for slide in slides:
          content = ''
          if ',' in slide:
            for sub_slide in slide.split(','):
              content += slide_content(sub_slide.strip())
            out.write('<section>{}</section>'.format(content)) 
          else:
            out.write(slide_content(slide))
        out.write(bottom)



