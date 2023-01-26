#import libraries needed
import numpy as np
import astropy.units as u
from ReadFile import Read #import Read function from ReadFile
#Function: To take calculate the magnitude distance, velocity and mass of a 
#          single particle with specific arguments describing the particle information
#Arguments: 
#          1)the exact location of the file including the name of the file, type=str
#          2)the type of particle, (1,2,3,etc) or (Disk,Halo,etc), type=str or int
#          3)the particle_# (starts from 0 and goes until number of rows-1), type=str
#Return: magnitude of the distance (kpc), magnitude of the velocity (km/s) 
#        and mass (M_solar)
def ParticleInfo(fileLoc, particle_type, particle_numb):
    time,total,data = Read(fileLoc)  #we only need data from this function
    mag_distance, mag_velocity = 0,0  #set the sumation to zero as the baseline
    for direction in ['x','y','z']:   #setting up the three directions
        pos_val = data[direction][np.where(data['type'] == particle_type)][particle_numb]*u.kpc
        mag_distance += pos_val**2  #adding squared distance to the total squared distance
        vel_val = data['v'+direction][np.where(data['type'] == particle_type)][particle_numb]*(u.km/u.s)
        mag_velocity += vel_val**2  #adding squared velocity to the total squared velocitie
    mag_distance, mag_velocity = (mag_distance)**0.5, (mag_velocity)**0.5  #taking the root to find magnitude
    mass = data['m'][np.where(data['type'] == particle_type)][particle_numb]*u.solMass  
    mass *= 10**10   #since the data records it in e^10
    return mag_distance, mag_velocity, mass
def main():
    #file with snapnumb = 000
    file_location = '''C:\\Users\mcorb\OneDrive\Desktop\School Work\School Year\Spring 2023\ASTR400B\Imports\MW_000.txt'''
    info = ParticleInfo(file_location,2,99)  #disk is particle_type=2, 100th particle = 100-1 (indexing)
    lyr_dist = info[0].to(u.lyr)  #converting distance into light year
    #below is the print statement of the final result
    print(f'''
    3D distance = {info[0]}
    3D velocity = {info[1]}
    mass = {info[2]}
    3D distance in lyr =  {lyr_dist}
    ''')  
main()