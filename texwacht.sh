
while true #run indefinitely
do 
        inotifywait -r -e attrib,close_write,move $1  &&   ./dolat.sh $1

done
