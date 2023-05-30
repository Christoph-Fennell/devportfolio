#This is my Pandas package import line
import pandas as pd

#Here I am creating a dictionary based on various Rifle specs
data = {"Rifle type": ["M-4", "M-14", "MSR"],
                    "Caliber": [ .556, .762, .338],
                    "Projectile mass (grams)": [3.56, 9.8, 13],
                    "Muzzle velocity (ft/s)": [3250, 2350, 2850],
                    "Rounds held": [30, 20, 8]}

#This line is creating a data frame that is based on the specifications in "data"
df = pd.DataFrame(data, columns = ['Rifle type', 'Caliber', 'Projectile mass (grams)', 'Muzzle velocity (ft/s)', 'Rounds held'])

#This is just a print statement for a sanity check 
print(df)

#The next three lines are locking the lens into that "Caliber" column and determining the class of the rifle
df.loc[df['Caliber'] == .556, 'Rifle class'] = "Infantry Rifle"
df.loc[df['Caliber'] == .762, 'Rifle class'] = "Marksman Rifle"
df.loc[df['Caliber'] == .338, 'Rifle class'] = "Sniper Rifle"

#Another print statement sanity check
print(f"\n{df}")

#This is just cleaning up my output
print("")

'''This statment is basically appending the Rifle class to the end of the data frame based on the Rifle type using Lambda functions
and then creating a new, smaller data frame that shows the rifle type and class for quick feedback
'''
print(df.apply(lambda row: row["Rifle type"] + ": " + str(row["Rifle class"]), axis = 1))

#These next two lines are locking the lens on Projectile mass for further data manipulation
select_column = df["Projectile mass (grams)"][1]
select_row = df.iloc[1]["Projectile mass (grams)"]

#This is creaating a list of values based on Muzzle energy
muzzle_energy = []

'''This for loop is iterating over the length of the Projectile mass column to mathematically create
the muzzle energy based on values found in Projectile mass as well as muzzle velocity and then appending 
those values to the Muzzle energy list
'''
for i in range(len(df)):
    energy = df["Projectile mass (grams)"][i] * (df["Muzzle velocity (ft/s)"][i]**2) / 2
    muzzle_energy.append(energy)

#This line is creating a new column called Muzzle energy to the most recently manipulated data frame
df["Muzzle energy (joules)"] = muzzle_energy

#Final sanity check and print statement
print(f"\n{df}")