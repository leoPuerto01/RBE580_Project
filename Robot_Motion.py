# Import the Client from ambf_comm package
# You might have to do: pip install gym
from ambf_client import Client
import pandas as pd
import time

# Create a instance of the client
_client = Client()

# Connect the client which in turn creates callable objects from ROS topics
# and initiates a shared pool of threads for bi-directional communication
_client.connect()

# You can print the names of objects found
print(_client.get_obj_names())

# Lets say from the list of printed names, we want to get the
# handle to an object named "Base Link"
obj = _client.get_obj_handle('baselink')
time.sleep(3)
obj.set_pos(0.5,0.5,0.5)
time.sleep(3)


tar = _client.get_obj_handle('target_ik')
time.sleep(3)
tar.set_pos(.1,.2,0)
time.sleep(.1)
tar.set_pos(.1,.5,0)
time.sleep(.1)
tar.set_pos(0.5,.2,0)
time.sleep(3)


# Load the Transformation Matrix
# If we have the entire T then 
# p = [T(1,4), T(2,4), T(3,4)];

#-------------------------------------------------------------------------------------------------------------------------------------------------------

# Next we import the data points as a list from the CSV file using Pandas. 
url = "https://raw.githubusercontent.com/leoPuerto01/RBE580_Project/main/matlab/davinci%20wrist%20sample.csv"

# Creating a list for coluns headers. This will be important when separating columns
col_list = ["Point1_X","Point1_Y","Point1_Z","Point2_X","Point2_Y","Point2_Z","Point3_X","Point3_Y", "Point3_Z"]

# Reading the cvs file from github. names=col_list
df = pd.read_csv(url, engine ='python', sep = ', ', names = col_list)

# Having issues where all the data is being shown in column 1 only. Therefore, since all this data is in this ne column, I am going to split the column
column = df.Point1_X

# Splitting the only column that contains all the data
test = column.str.split(',', expand=True)

# Storing the XYZ values of each point in 1 List. Size is n x 3 matrix
Point1_xyz = np.matrix([test[2], test[3], test[4]])
Point2_xyz = np.matrix([test[8], test[9], test[10]])
Point3_xyz = np.matrix([test[14], test[15], test[16]])

# Create 3 lists for 3 points 
# I think we will only be using tool tip list as of now

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Multiply the 1,2,3 column with p vector
# Multiply with a scaling factor
# Hint: Choose the Scaling factor such that the point comes under 2m example 200*x <=  2

# then create a loop that iterates over the list and set pos to (x,y,z)
for i in range(len())
  # list list and set pos to (x,y,z)
  time.sleep (0.2)
