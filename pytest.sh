
while true #run indefinitely
do 
        inotifywait -r -o ~/watchtool/log -e access,modify,attrib,close_write,move $1  &&  python  $1 ; echo ""; echo "---"; echo "" 

done
