# Assignment_1 README
Online Portfolio Assignment 1 GEOG5003M


This software takes in coordinate data from an external source and assigns them to agents. These agents will then move around an environment randomly, interacting with the environent as they 'eat away' from it.

External Data Source: https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html

When the software is run, the user will be asked to input integer values for the number of agents (up to 100), the number of iterations (number of random movements around the environment) and the neighbourhood distance (the distance between agents at which storage data may be shared between them).




This software can be run within a python reader, or directly from a command prompt.  
If run directly within a command prompt, the following variables can be inputted as follows:

`python model.py x y z`

where 
* x = Number of Number of Agents (integer < 100)
* y = Number of Iterations (integer)
* z = Neighbourhood Distance (integer)



Known Issues:

* The program may break if the number of agents inputted is greater than 100. This is due to there only being 100 coordinates stored in the original external data source.
