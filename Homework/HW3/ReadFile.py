#import what you need
import astropy.units as astr
import numpy as np
#function: To get a file and extract the information frmo the first line, second line
#          and the rest of the data starting from line 4 into a sepcial numpy array
#Argument: location of file on your computer, including its name, assumed to be string
#Return: time is the total time of the system, total is the total number of particles
#        and data is a special numpy array.
def Read(file_location):
    file = open(file_location, 'r')
    #takes the first line (assumed to be label,value format) and records only 
    #the value, convert to float and attach units of Myr
    time = float(file.readline().split()[1])*astr.Myr 
    #takes second line, that has same formatting, however total has to be
    #integer since particles are whole numbers
    total = int(file.readline().split()[1]) 
    file.close()  
    #gets the rest of the data starting from line 4 until the end of the file
    #and stores it in a special list with format 
    #[column_type i.e(#type,m,x,y,z,vx,vy,vz)][row_#]
    #type# meaning --> 1=DarkMatter, 2=DiskStars 3=BulgeStars
    data = np.genfromtxt(file_location,dtype=None,names=True,skip_header=3)
    return time, total, data
def main():
    #a test function to make sure that the code above works
    file_location = '''C:\\Users\mcorb\OneDrive\Desktop\School Work\School Year\Spring 2023\ASTR400B\Imports\MW_000.txt'''
    time, total, data = Read(file_location)
main()