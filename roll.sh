#!/bin/bash
echo "Rolling Dice"

#save dice numbers.
DICE="diceroll.txt"

# save dice logs
LOG="dice.log"

DICE1=$((1 + RANDOM % 6))
DICE2=$((1 + RANDOM % 6))
LASTROLL=$(tail -1 $DICE)
POINT=$(head -n 1 $DICE)

if [[ $LASTROLL =~ ^[0-9]+$ ]];then
    echo "Last roll was: $LASTROLL and the Point is: $POINT" >> $LOG
else
    echo "Establishing a new point" >> $LOG
fi

TOTAL=$((DICE1+DICE2))

WINNERS=(7,11)
CRAPPERS=(2,3,12)

HARDWAYS=(2,4,6,8,10)

echo "DICE(1) is $DICE1 and DICE(2) is $DICE2 for a total of $TOTAL" >> $LOG

if [ -z "$LASTROLL" ]; then
    #First Roll Goodies

    if [[ "${CRAPPERS[@]}" =~ "${TOTAL}" ]]; then
        
        if [[ $TOTAL == 3 ]]; then
            echo "3 crap, son of a yo!" >> $LOG
        elif [[ $TOTAL == 12 ]]; then
            echo "12 crap, Big Daddy in the rice paddy" >> $LOG
        elif [[ $TOTAL == 2 ]]; then
            echo "Ohhhhh Snakeyes!" >> $LOG
        fi

    elif [[ "${WINNERS[@]}" =~ "${TOTAL}" ]]; then 
        echo "Winner Winner - Pay the roller!!!" >> $LOG
    else
        echo $TOTAL >> $DICE
    fi

elif [[ $TOTAL == $LASTROLL ]]; then
    echo "We have a winner!!" >> $LOG
    echo -n "" > $DICE

elif [[ $LASTROLL > 0 && $TOTAL != "7"  ]]; then
    #live to see another day
    if [[ "${HARDWAYS[@]}" =~ "${TOTAL}" ]]; then
        if [[ $DICE1 == 1 && $DICE2 == 1 ]]; then
            echo "Ohhhhh Snakeyes!" >> $LOG
        elif [[ $DICE1 == 2 && $DICE2 == 2 ]]; then
            echo "Shooting that Ballerina!" >> $LOG
        elif [[ $DICE1 == 3 && $DICE2 == 3 ]]; then
            echo "Hard Six!" >> $LOG
        elif [[ $DICE1 == 4 && $DICE2 == 4 ]]; then
            echo "Square Pair...!" >> $LOG
        elif [[ $DICE1 == 5 && $DICE2 == 5 ]]; then
            echo "Ahhhh Puppy Paws !! " >> $LOG
        fi
        #the roll keeps going
        echo $TOTAL >> $DICE
    else
        #the roll keeps going
        echo $TOTAL >> $DICE
    fi
        if [ -z ${POINT} ]; then 
            echo "Nice $TOTAL! Let's keep the dice hot and hit that $TOTAL" >> $LOG
        else 
            echo "Nice $TOTAL! Let's keep the dice hot and hit that $POINT!" >> $LOG
        fi
else
    # we have crapped out.
    echo "Seven out, cinco dos, adios! Thanks for the bets and don't forget to tip your dealers!" >> $LOG
    # clear the dice.
    echo -n "" > $DICE
fi


