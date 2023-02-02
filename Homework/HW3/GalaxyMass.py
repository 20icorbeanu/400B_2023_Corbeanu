#Import what needs to bo be imported
import numpy as np
import astropy.units as u
from ReadFile import Read 
#Function: To take in a file location, collect al the masses from a certain type of particle
#          where the particle type is an integer and sum all those masses into one value with
#          units of Solar Mass 1e12.
#Arguments:
#         1)File location is a string that points to where the file you want to read is located
#         2)Particle type is an integer where 1=Dark Matter, 2=Disk matter, 3=Buldge matter
#Return: Returns the total solar mass in units of SOlar Mass 1e12
def ComponentMass(file_location, particle_type):
    time, total_particles, data = Read(file_location)  #we ignore time and total_particles
    #collecting all mass under data array under condition of the particle type
    mass_lst_particle_type = data['m'][np.where(data['type'] == particle_type)] 
    #start the sumation of all the values in the lst made above 
    total_particle_type_mass = 0 
    for particle_mass in mass_lst_particle_type:
        total_particle_type_mass += particle_mass
    #since mass from txt given in 1e10, to get answer in 1e12, we deveide answer by 100
    total_particle_type_mass /= 100
    #return result with units (using astropy) and rounded to nearest 3 decimal places
    return np.round(total_particle_type_mass, 3)*u.solMass

#function to test the previous function and get mass of each component in 3 galaxies (MW,M33,M31),
#the total mass of each galaxy, the cumalitive mass of all three, and the baryon factor which is
#computed by f_bar=total_stellar_mass/total_mass_stellar+dark for all three and each galaxy
def main():
    galaxy_names = ['MW','M33','M31']  #to make it easier to adjust code if we want more galaxies
    #create dictionary with style GalaxyName_ParticleNumber. Example MW_1 is milkyway particle type1
    galaxy_dic = {}
    for name in galaxy_names:
        for particle in [1,2,3]:
            mass = ComponentMass(f'''C:\\Users\mcorb\OneDrive\Desktop\School Work\School Year\Spring 2023\ASTR400B\Imports\{name}_000.txt''',particle)
            galaxy_dic[name+'_'+str(particle)] = mass  #creating naming scheme with mass
    #print the mass of each particle type for each galaxy
    print('---Individual Masses---')
    for name_part, mass in galaxy_dic.items():  #loops each mass in dictionary and prints them nicely
        print(f'{name_part} = {mass}')
    #getting dictionary for total mass of each galaxy
    total_mass_dict = {}  
    mass_tot = 0
    i,j = 0,0  #iterations we set up. i is the # of particles (const 3) and j will go for number of galaxies
    for name_part, mass in galaxy_dic.items():
        if i==3:     #since 3 particle types, i caps at 3
            i, mass_tot= 0,0
            j += 1
        i += 1
        mass_tot += mass
        total_mass_dict[galaxy_names[j]] = mass_tot
    #printing total mass for each galaxy and total mass
    print('---Total Mass---')
    total_mass = 0
    for name_part, mass in total_mass_dict.items():
        print(f'{name_part} = {mass}')  #iterate dic and print nicely
        total_mass += mass
    print(f'Local_Group_Mass = {np.round(total_mass,3)}')
    #getting dictionary mass for sum of first two particle types
    mass_1_2_dic = {}
    mass_tot = 0
    i,j = 0,0
    #same logic as above, however we need to skip the third group, thus i=2 and we iterate on else to skip.
    for name_part, mass in galaxy_dic.items():
        if i==2:   
            i, mass_tot= -1,0
            j += 1
        else:
            mass_tot += mass
            mass_1_2_dic[galaxy_names[j]] = mass_tot
        i += 1
    tot_mass_1_2 = 0
    for name,mass in mass_1_2_dic.items():
        tot_mass_1_2 += mass  #iterate through each mass and sum them up for total.
    #printing baryon fraction for each galaxy and local group
    print('---Baryon Number---')
    for (name,mass_tot), (name,mass_1_2_tot) in zip(total_mass_dict.items(),mass_1_2_dic.items()):
        print(f'{name} = {np.round(mass_1_2_tot/mass_tot,3)}')  
    print(f'Local_Group = {np.round(tot_mass_1_2/total_mass,3)}')

main()
