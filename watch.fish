#!/usr/bin/env fish

inotifywait -c -e modify,create,delete -mr ./ | while read line
    set dir (echo $line | cut -d, -f1)
    set file (echo $line | cut -d, -f3)
    if [ "$dir" = "./slides/" -o "$dir" = "./sets/" ]
    	./build.py a
    end
    switch $file
      case '*.slides'
        ./build.py a
    end
end