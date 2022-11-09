# Final Project - https://www.hockey-reference.com/players/o/ovechal01.html
# Karanjot Bassi - 30094007
# lab 08
# The only information I needed for this infographic was the stats of the player in the last 10 years, everything else was extra info 
# that was not needed, so for my data cleaning I deleted all extra information and kept all that was needed 

from SimpleGraphics import *
import random

def get_text(): # this line of code will read my csv file and give me the content i need. No parameter is required because path is put in directly
    content = open("/Users/karanjotbassi/Documents/School stuff/Winter 2021/Data 211/Data Code/Final Project/data_clean.csv", "r")
    content = content.readlines()
    content = content[1:]
    count = 0
    for i in range(len(content)):   #doing this will give me my data that i will use in a very clean and easy way to use. 
        content[i] = content[i].strip()
        while ('') in content:
            content.remove('')
            content.close()
    return content #content will be returned because I will need to use the information later on 

def background():   #This is an extra line of code which will set a background colour for my infograph (No parameter), no return
    setFill("lavender")
    rect(0, 0, 800, 600) #It was not neccessary for me to resize the window as everything was able to fit 

def title(): #This is the title of the infograph, no parameter needed, no return
    setFont("Times", "20", "Bold")
    text(400, 25, "Alex Ovechkin 2011-2020 Stats")

def explanation():  #paragraph that gives an overview of the infograph, no parameter needed and no return 
    setFont("Times", "12", "bold")
    text(520, 125, 
    "NHL All-star Alex Ovechkin has been dominating" "\n" 
    "since being drafted back in 2006. Well into his" "\n"
    "mid 30's he is still scoring and is considered" "\n"
    "one of the best goal scorers in history. As" "\n"
    "he is getting older, I have taken a look at his" "\n"
    "past 10 years. In the following graphs I have taken a" "\n"
    "look at his stats. Points(Pt), Goals(G), Assists(A)," "\n"
    "Games played(GP) and age to determine if he will" "\n" 
    "countine to dominate or slow down in the near future.", "w")

def bar_axis(): #no parameter needed, this line will generate the axis for the bar graph, 
    y_axis = line(50, 100, 50, 200) # I chose to do this seprate as it cleaner and easier to look back at if change is required 
    x_axis = line(50, 200, 500, 200)
    setFont("Times", "15")
    title = text(225, 75, "Last four Seasons (GP + G + A)")
    y_orgin = 200
    orgin = 0
    while orgin <= 100:
        setFont("Times", "10")
        text(40, y_orgin, orgin)
        y_orgin -= 20
        orgin += 20     #no return value is needed as axis will be generated

def bar_elements(content):  # to get the content needed easy to generate the bars, in bar graph, use parameter content 
    bar_data = content[6:10] # to return bar data of the elements needed for the graph(the previous 4 years)
    return bar_data #return bar data

def bar_chart(bar_data): #to generate bars in graph, put in parameter bar data
    element = 0
    x_orgin_GP = 50 #these will be set for the orgin points for the 3 bars 
    x_orgin_G = 75
    x_orgin_A = 100
    while element != 4:
        data = bar_data[element].split(",") #split the elements so we can call on the specific element needed
        setFill("light sky blue")
        rect(x_orgin_GP, 200, 25, -int(data[1])) #call on the elements and create the bar for that element, different colour for each 
        setFont("Times", "10", "Bold")
        text((x_orgin_GP + (x_orgin_GP+25))/2, 205 - int(data[1]), data[1])
        setFill("green")
        rect(x_orgin_G, 200, 25, -int(data[2]))
        setFont("Times", "10", "Bold")
        text((x_orgin_G + (x_orgin_G+25))/2, 205 - int(data[2]), data[2])
        setFill("red")
        rect(x_orgin_A, 200, 25, -int(data[3]))
        setFont("Times", "10", "Bold")
        text((x_orgin_A + (x_orgin_A+25))/2, 205 - int(data[3]), data[3])
        x_orgin_A += 125
        x_orgin_G += 125
        x_orgin_GP += 125
        element += 1    # set new orgin for the next set of elements, and += 1 to element to eventually end loop. No return needed

def bar_legend(): #legend for the bar graph, tells you what each bar represents, no parameter needed and no return 
    setFill("light sky blue")
    rect(162.5, 220, 10, 10)
    text(183, 225, "GP")
    setFill("green")
    rect(275, 220, 10, 10)
    text(296, 225, "G")
    setFill("red")
    rect(387.5, 220, 10, 10)
    text(408, 225, "A")

def line_axis(): #no parameters needed and no return, simply to just make the outline of the scatter plot. 
    y_axis = line(550, 275, 550, 475)
    x_axis = line(550, 475, 775, 475)
    setFont("Times", "10")
    axis = text(662.5, 485, "2011-2020")
    orgin_axis = 0
    y_orgin = 475
    x_orgin = 550
    while orgin_axis <= 100:
        setFont("Times", "10")
        text(x_orgin - 10, y_orgin, orgin_axis)
        y_orgin -= 40
        orgin_axis += 20
    setFont("Times", "15")
    title = text(670, 250, "Ovechkins Pts, G and A")
    setFill("green")
    ellipse(606.25, 500, 10, 10)
    setFont("Times", "10")
    text(600, 505, "G")
    setFill("red")
    ellipse(662.5, 500, 10, 10)
    setFont("Times", "10")
    text(655, 505, "A")
    setFill("gold")
    ellipse(718.75, 500, 10, 10)
    setFont("Times", "10")
    text(710, 505, "Pts")

def scatter_lines(): # this is to create the boxes in the scatter, no parameter or return
    x_orgin = 550
    x_horzontal = 575
    y_orgin = 475
    y_horizontal = 275
    while x_horzontal <= 775:       #this will loop untill on the horizontal lines are completly drawn 
        line(x_horzontal, y_orgin, x_horzontal, y_horizontal)
        x_horzontal += 25
    while y_horizontal <= 475:  # keep looping untill the vertical lines are drawn 
        line(x_orgin, y_horizontal, 775, y_horizontal)
        y_horizontal += 40    # no return 

def line_content(content): #this is to generate the points in the scatter plot, parameter needed is content, no return. 
    element = 0
    x_orgin = 545
    y_orgin = 475
    while element!= 10:
        line_data = content[element].split(",") #since we are looking at all 10 years we need to call on all the elements to split 
        del(line_data[1])       #this step in not needed as it is just to make it easier to call on the index needed
        del(line_data[0])
        setFill("green")
        ellipse(x_orgin, y_orgin - 2 * int(line_data[0]), 10, 10)
        setFill("red")
        ellipse(x_orgin, y_orgin - 2 * int(line_data[1]), 10, 10)
        setFill("gold")
        ellipse(x_orgin, y_orgin - 2 * int(line_data[2]), 10, 10)
        element += 1        # loop will countine for each set of elements until data is completely generated
        x_orgin += 25

def pie_content(content):   #This is to get the total value of the pie chart, parameter is content and return is the total value
    list_count = 0
    total = 0
    while list_count != 6:
        pie_data = content[list_count].split(",")
        del(pie_data[3]) # this part is not needed, makes the looping and data collection a little easier to see which data is collected
        del(pie_data[2])
        del(pie_data[1])
        total += int(pie_data[1])
        list_count += 1
    pie_Total = total
    return pie_Total #retunred is the total value of the pie chart so that it can be used when making the sectors in the pie chart

def pie_title(): #no parameter needed, this is just the title for the bar chart, easy to change if needed and no return
    setFont("Times", "15")
    text(130, 265, "First five seasons (Age + Points)")

def pie_chart(content, pie_Total): #generating the pie chart needs 2 parameters, content and the pie chart total value found earlier
    element = 0
    startAngle = 0
    redvalue = random.randint(0, 255)
    bluevalue = random.randint(0,255)
    greenvalue = random.randint(0,255) #calling the random so that different colour sectors will be generated 
    y_orgin = 315
    setFont("Times", "10") # the age corresponding with the total points will be listed 
    text(240, 305, "Age")
    while element != 6: # need to loop through the first 5 seasons (2011 - 2015) 
        pie_data = content[element].split(",")
        setFill(redvalue, greenvalue, bluevalue)
        pieSlice(20, 280, 200, 200, startAngle, int(pie_data[4])/pie_Total*360)
        setFill(redvalue, greenvalue, bluevalue)
        rect(250, y_orgin, 10, 10)
        setFont("Times", "10")
        text(240, y_orgin + 5, pie_data[0]) 
        redvalue = random.randint(0,255)        #reset random colours to get different colour sectors 
        bluevalue = random.randint(0,255)
        greenvalue = random.randint(0,255)
        y_orgin += 30
        startAngle += int(pie_data[4])/pie_Total*360 #next angle starts where last angle stopped 
        element += 1 # no return value 


def chart_explanation(): # this is further detail for the infograph, no parameters or return.
    setFont("Times", "12", "bold")
    text(300, 375,
    "The bar chart displays Ovechkin's" "\n"
    "goals(G), assists(A) and games" "\n"
    "played in the last 4 hockey seasons." "\n"
    "The pie chart displays his age and" "\n"
    "total points he got at that age in" "\n"
    "his first 5 seasons starting in 2011." "\n"
    "Finally the scatter shows the trend in" "\n"
    "points(Pt), goals(G) and assists(A) in" "\n"
    "the last 10 years. From this data we can" "\n"
    "conclude that his age hasn't stopped his" "\n"
    "ability to produce in the NHL. The GP in" "\n"
    "2020 were reduced due to covid and we can" "\n"
    "see from the data that if NHL countinued" "\n"
    "play there was a high chance Ovechkin" "\n"
    "would have scored more than in his past" "\n"
    "5 seasons. We can assume if he stays healthy" "\n"
    "Ovechkin will be able to keep producing.", "w")

def main(): # call each function in order, no parameter or return
    content = get_text()
    background()
    explanation()
    title()
    bar_axis()
    bar_legend()
    bar_data = bar_elements(content)
    bar_chart(bar_data)
    line_axis()
    scatter_lines()
    line_content(content)
    pie_title()
    pie_Total = pie_content(content)
    pie_chart(content, pie_Total)
    chart_explanation()

main() # call main