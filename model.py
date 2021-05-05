import sys
import random
import matplotlib.pyplot
import matplotlib.animation
import agentsframework
import csv
import tkinter
import requests
import bs4
import matplotlib
matplotlib.use('TkAgg')


# Taking co-ordinate information from a web page
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
tdsy = soup.find_all(attrs={"class" : "y"})
tdsx = soup.find_all(attrs={"class" : "x"})
tdsz = soup.find_all(attrs={"class" : "z"})



num_of_agents = []
num_of_iterations = []
neighbourhood = []
environment = []
rowlist = []
agents = []


'''Set up user inputs for number of agents, number of iterations and 
neighbourhood distance either directly from the command line or from user 
input'''

# Input from the command line
try:

    print(sys.argv)                                         
    print(type(sys.argv))
    num_of_agents = int(sys.argv[1])
    num_of_iterations = int(sys.argv[2])
    neighbourhood = int(sys.argv[3])

    print("Number of Agents: ", num_of_agents)
    print("Number of Iterations: ", num_of_iterations)
    print("Neighbourhood Distance: ", neighbourhood)


# Input from python user input
except:
    
    while True:
        try:
            num_of_agents = int(input("Type Number of Agents "))
            if num_of_agents > 100:
                raise ValueError
            if num_of_agents < 0:
                raise ValueError
            break
        except ValueError:
            print("")
            print("**ERROR** Please enter a positive integer value between " +
                  "0 and 100 for the number of agents")
        
    while True:
        try:
            num_of_iterations = int(input("Type Number of Iterations "))
            if num_of_iterations < 0:
                raise ValueError
            break
        except ValueError:
            print("")
            print("**ERROR** Please enter a positive integer value for the " + 
                  "number of iterations")
         
    while True:
            try:
                neighbourhood = int(input("Type Neighbourhood Distance "))
                if neighbourhood < 0:
                    raise ValueError
                break
            except ValueError:
                print("")
                print("**ERROR** Please enter a positive integer value for " +
                      "the neighbourhood distance")        
                
    print("")
    print("")            
    print("Number of Agents: ", num_of_agents)
    print("Number of Iterations: ", num_of_iterations)
    print("Neighbourhood Distance: ", neighbourhood)
        


# Creation of environment inputted from another source
f = open('in.txt', newline = '')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:                      
    rowlist = []
    environment.append(rowlist)                                  
    for value in row:                                       
        rowlist.append(value)
f.close()


# Make the agents.
for i in range(num_of_agents):
    y = int(tdsy[i].text)
    x = int(tdsx[i].text)
    agents.append(agentsframework.Agent(environment, agents, y, x))

# Make figure for agents to move within
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])


# Move and animate the agents
def update(frame_number):
    
    fig.clear()

    for j in range(num_of_iterations):
        for i in range(num_of_agents):
            agents[i].move()
            agents[i].eat()
            agents[i].shared_with_neighbours(neighbourhood)
            random.shuffle(agents)
        
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.ylim(0, 99)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
        
    matplotlib.pyplot.imshow(environment)
    
    
# Make command to run in tkinter
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, 
    interval=20, repeat=False, frames=num_of_iterations)
    canvas.draw()
    label_widget = tkinter.Label(root, text="Agents interacting with " +
    "environment")
    label_widget.pack()


# Make GUI using tkinter 
root = tkinter.Tk()
root.wm_title("Model")
label_widget = tkinter.Label(root, text="Run the model by selecting it " + 
"from the menu above.")
label_widget.pack()
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

tkinter.mainloop()



