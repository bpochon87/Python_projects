# Import dattime and timezone modules
# Display Portland 9-5 hours in Pacific
# Display London in Greenwich Mean Time
# Display NY in Eastern

import datetime
import pytz


# Get user input on whether or not they want Portland, NY, or London office.
# An option to print all branch hours and if they're closed will be included.

def getBranch():
    print("You may ask for a specific branch to see if they're open or closed or you may ask to see all branches and their current status.")
    branch = input("\nPlease enter Portland, London, NYC, or All: ").capitalize()
    if branch == 'Portland':
        portlandBranch()
    elif branch == 'London':
        londonBranch()
    elif branch == 'Nyc':
        nycBranch()
    elif branch == 'All':
        allBranches()
    else:
        print("\n\nPlease provide an entry from the list provided.\n\n")
        getBranch()

def portlandBranch():
    # Import Pacific timezone for this branch.
    # Convert that 24-hr based time to 12-hr based time
    # Compare that time to current time
    # If that time is within the 9-5 range, it's open. Else, it's false.
    closedStr = '17:00'
    openStr = '9:00'
    closed = datetime.datetime.strptime(closedStr, '%H:%M')
    opened = datetime.datetime.strptime(openStr, '%H:%M')
    
    print(closed)
    print(opened)
    
    #dtPacific = datetime.datetime.now(tz=pytz.timezone('US/Pacific'))
    #if dtPacific > opened and dtPacific < closed:
    #    print("The Portland branch is currently open.")
    #else:
    #    print("The Portland branch is currently closed.")




def londonBranch():
    dtLondon = datetime.datetime.now(tz=pytz.timezone('Europe/London'))
    print(dtLondon)
    



def nycBranch():
    dtNyc = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))
    print(dtNyc)
    
    
    
    
    
    
    
    

























if __name__ == "__main__":
    getBranch()
            
