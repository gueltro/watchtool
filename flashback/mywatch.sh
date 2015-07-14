##watch input directory


while true #run indefinitely
do 
	change=$(inotifywait -r -q -e attrib,close_write,move,modify,delete $1 )
	change=${change#./ * }
	python  backup.py $change
done
