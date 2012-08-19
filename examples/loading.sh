
terminal_width=`tput cols`
terminal_height=`tput lines`

index=`od -An -N2 -i /dev/random`
index=$(( index %= 500 ))

URLBASE="http://animals.ivolo.me"

counter=0
increment=1
offset=0
steps=10


step () {
    offset=$((offset + increment))
    if [ $(( offset % steps )) -eq 0 ]
    then
        increment=$(( increment * -1))
        terminal_width=`tput cols`
        terminal_height=`tput lines`
    fi

    [ $increment -eq 1 ] && reverse="false" || reverse="true"
    [ $counter -eq 0 ] && terminal="false" || terminal="true"

    url="$URLBASE/?index=$index&offset=$offset&reverse=$reverse&terminal=$terminal&maxwidth=$terminal_width&maxheight=$terminal_height"

    curl -s "$url"

    counter=$(( counter + 1))
}

while true
do
    step
    sleep 0.2
done

echo ""
