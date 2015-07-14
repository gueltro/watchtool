
while true #run indefinitely
do 
        inotifywait -r -o ~/watchtool/log -e access,modify,attrib,close_write,move $1  &&  (clear ;/home/gueltro/6.945/artifacts/bin/mit-scheme  --silent <  $1 ; echo ""; echo "---"; echo "" )
#        inotifywait -r -o ~/watchtool/log -e access,modify,attrib,close_write,move $1  &&  (clear ;/home/gueltro/6.945/artifacts/bin/mit-scheme   <  $1 ; echo ""; echo "---"; echo "" )


done
