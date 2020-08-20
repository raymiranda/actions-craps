# Python
#
# This file implements an example.
#
# This file is part of mdutils. https://github.com/didix21/mdutils
#
# MIT License: (C) 2018 Dídac Coll


from mdutils.mdutils import MdUtils
from mdutils import Html
import os, re, csv

mdFile = MdUtils(file_name='README', title='Let\'s Roll Some Dice!')

# Testing string format.
string = """
The goal was to create simple example using Github Actions but, somehow that morphed into playing a game of Craps. \n
I've learned that creating something `fun` will help you to retain all the learning steps taken to develop something. \n
During the workflow, we will use a simple bash script to simulate the `roll` and log the output to a text file.\n
That text file will then be stored in the repository and parsed to display at the bottom of this README file. \n
I wanted to demonstrate how utilizing `MdUtils` will make writing Markdown files extremely easy. \n

What I tested during this process: \n
- Saving diceroll.txt to an artifact. \n
- Saving diceroll.txt as a cache/key. \n
- Establishing a lambda call utilizing an AWS API Gateway. \n
In the end, I chose to save the file in the repository to allow anyone to pick up the dice as the shooter. \n.
I'll expand more in my blog but for now, let's start rolling! \n
New Shooooooooooooooooooootaaaaa!!"
"""

# style is set 'atx' format by default.
mdFile.new_header(level=1, title='Overview')  
mdFile.new_paragraph(string)

#Overview information
mdFile.new_header(level=1, title='Let\'s Play!')
mdFile.new_paragraph("Welcome to Casino Del Ray. This is a simple game of Craps that incorporates some of the sayings that you would normally hear around the table."
" If you’ve never played craps, you’re seriously missing out (unless you’re coding, in which case you will inevitably make more $$ doing that in the long run).")

mdFile.new_paragraph("**IMPORTANT:** This game will not teach you <ins>strategery</ins> or make you a pro. All bets are off..... (I'm not liable for any real $$ lost at the table)", bold_italics_code='bi', color='purple')
# How to play
mdFile.new_header(level=1, title="Rules of the Game")
mdFile.new_header(level=2, title="Come Out Roll")
mdFile.new_paragraph("This is where the `point` is established. The dice you're about to roll will either make you a hero or zero real quick. Good Luck!")
mdFile.insert_code("First Roll: \n"
                   "\n"
                   "7, 11 = Immediate winner! If you bet on the ``Pass Line``, you win and get to roll again!.\n"
                   "2, 3, 12 = Craps. If you roll any of these numbers on the first roll, you lose your $$. The funny thing is that you also get to roll again if you choose to do so. \n"
                   "Note: On a craps roll, you would have won if you bet on the ``Don\'t Pass`` line, but that's risky. \n"
                   "4, 5, 6, 8, 9, 10 = Establish the point on the first roll and the game continues. \n"
                   "\n"
                   "Note... note...: Some people are very superstitious when it comes to Craps so beware if you start to bet `against` the table, although I've seen some rollers do very well. \n"
                   "At the end of the day, it's your $$, so you choose your own destiny. \n"
                   "Note... note... note...: Always Tip your dealers. They help you understand the game better and are extremely patient as you learn the game!"
                   , language='php')


imagelink = "https://media.tenor.com/images/9081df2ca9610e3fdb4e0dfca1b27df1/tenor.gif"
imagetext = "Rick Roll Eyes"

mdFile.new_header(level=2, title="Second Roll and Forward")
mdFile.new_paragraph("If you didn't win on your first roll and you've established the point, the goal is to roll the number again. \n")

mdFile.new_paragraph(Html.image(path=imagelink, size='300x200', align='left'))
mdFile.new_paragraph("Yes, I know... easier said than done.  \n")
mdFile.new_paragraph("The odds are stacked against you since ``7`` is the highest probability to roll with 6 and 8 following.  \n"
            "Hit the established point and you win! Roll a 7 and its game over.")


mdFile.new_header(level=1, title="Current Dice Game")


with open('dice.log', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter='\n')
    rows = list(reader)
    if len(rows) > 2: 
        last_line = ' '.join(rows[-1])
        last_saying = ' '.join(rows[-3]) + ' '+ ' '.join(rows[-2])
    elif len(rows) == 2: 
        last_line = ' '.join(rows[-1])
        last_saying = ' '.join(rows[-2])

    else: 
        # last shot was a craps or winner.
        last_saying = ' '.join(rows[-1])

if os.stat("diceroll.txt").st_size == 0: 
    mdFile.new_paragraph(last_saying)
    # Get the current dice roll.
    mdFile.new_header(level=2, title="Need a new shooter!")
    link = "https://github.com/raymiranda/actions-craps/issues/new?title=Roll%20Some%20Dice&body=https://api.github.com/repos/raymiranda/action-craps/issues?title=Let%27s%20Roll%20Some%20Dice&body=Add%20your%20own%20comments"
    text = "--> We need a new shooter! <--"
    mdFile.new_line(mdFile.new_inline_link(link=link, text=text))
else: 
    d = last_line.strip().replace(" ", "").split("|")
    point = d[2]
    dice = d[1].split(",")
    dice1 = './images/'+str(dice[0])+'.png'
    dice2 = './images/'+str(dice[1])+'.png'
    last_roll = re.sub("[^0-9]", "", d[0])

    if "lets try to hit that" in last_saying:
        mdFile.new_header(level=2, title="The point is now " + str(last_roll) +"! Let's go shooter!")
    else: 
        mdFile.new_header(level=2, title="Last roll was a " + str(last_roll) +"! The point is "+str(point))
    

    mdFile.new_line(mdFile.new_inline_image(text='Dice 1', path=dice1))
    mdFile.new_line(mdFile.new_inline_image(text='Dice 2', path=dice2))

    link = "https://github.com/raymiranda/actions-craps/issues/new?title=Roll%20Some%20Dice&body=https://api.github.com/repos/raymiranda/action-craps/issues?title=Let%27s%20Roll%20Some%20Dice&body=Add%20your%20own%20comments"
    text = "--> The Dice Are Hot - Keep It Going! <-- "
    mdFile.new_line(mdFile.new_inline_link(link=link, text=text))


# Create a table of contents
mdFile.new_table_of_contents(table_title='Contents', depth=2)
mdFile.create_md_file()
