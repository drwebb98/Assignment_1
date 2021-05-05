# Assignment_1 README
**Online Portfolio Assignment 1 GEOG5003M**


This software takes in coordinate data from an external source and assigns them to agents. These agents will then move around an environment randomly, interacting with the environent as they 'eat away' from it.

External Data Source: https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html

When the software is run, the user will be asked to input integer values for the number of agents, the number of iterations and the neighbourhood distance (see below).  
Running the programme will produce an animation of the agents interacting with the environment within matplotlib, presented within a GUI created using tkinter.

***

**Variables:**

`num_of_agents` = Number of agents to move around the environment (integer <100; input)  
`num_of_iterations` = Number of random movements the agents make around the environment (integer; input)  
`neighbourhood` = The neighbourhood distance between agents at which storage data may be shared between them (integer; input)  
`environment` = Height data used to create an environment for the agents to move around in (integer)  
`rowlist` = Environment data for a single row of data (integer)  
`agents` = The agents to move around the environment  

*class* `Agent()`  
  `move` = Moving the agents   
  `eat` = Removal of height data from the environment and addition to the storage of agents  
  `distance_between` = Calculates the distance between agents  
  `shared_with_neighbours` = Sharing of stored data between agents if they are within a defined distance of each other


***

This software can be run within a python interpreter, or directly from a command prompt.  
If run directly within a command prompt, the following variables can be inputted as follows:

`python model.py x y z`

where 
* x = Number of Number of Agents (integer < 100)
* y = Number of Iterations (integer)
* z = Neighbourhood Distance (integer)

***

The user inputs for `num_of_agents`, `num_of_iterations` and `neighbourhood` must be positive integer values.  
The input for `num_of_agents` must also be <= 100.  
If they are not then error messages will alert the user to input an integer value and prompt them to try again until an acceptable value is provided. These tests are present to stop the programme from breaking.

***

Known Issues:

* The programme is restricted to <= 100 agents and may break if the number of agents inputted is greater than 100. This is due to there only being 100 coordinates stored in the original external data source. The programme currently restricts users from inputting values outside of this, but only if done within a python interpreter (the programme may still break if unaccepted inputs are made directly in the command prompt).

***

Further Development:

* Fix so that more than 100 agents can be used by creating random points for any agents other than the 100 already assigned coordinates.
* Update code for command prompt input to reduce the risk of the programme breaking if the number of agents exceeds 100 or if the inputs are not integers.
* Use `get()` and `set()` to protect the variables.
