
terminal_width=`tput cols`
terminal_height=`tput lines`

index=`od -An -N2 -i /dev/random`
index=$(( index %= 500 ))

URLBASE="http://animals.ivolo.me"

counter=0
increment=1
offset=0
steps=10

calculate_max_steps () {

    url=${1}

    animal="`curl -s "$url"`"

    maxlen=0

    export IFS="\n"
    for word in $animal; do
        len=`expr length "$word"`
        if [ $len -gt $maxlen ]
        then
            maxlen=$len
        fi
    done

    animal_width=$((maxlen - offset))
    steps=$(( terminal_width - animal_width))
}

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
