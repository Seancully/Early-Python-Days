# BMI Program that calculates the BMI of a person based on their weight in kg and height in meters, /
# but also calculates the BMI of a person based on their weight in pounds and height in inches


# Calculation for BMI with weight in kg and height in meters
# User input of height in meters
HeightMeters = input('Enter your height in meters:\n')
HeightMeters = float(HeightMeters)

# User input for weight in kg
WeightKG = input('Enter your weight in kg:\n')
WeightKG = float(WeightKG)

# BMI Calculation
BMI1 = WeightKG / (HeightMeters * HeightMeters)
print('\nYour BMI:', BMI1)


# Calculation for BMI with weight in pounds and height in inches
# User input for height in inches
HeightInches = input('\nEnter your height in inches:\n')
HeightInches = float(HeightInches)

# User input for weight in pounds
WeightPounds = input('Enter your weight in pounds:\n')
WeightPounds = float(WeightPounds)

# Converting inches to meters
HeightInches = HeightInches * 0.0254

# Converting pounds to kg
WeightPounds = WeightPounds * 2.25

# BMI Calculation
BMI2 = WeightPounds / (HeightInches * HeightInches)
print('\nYour BMI: ', BMI2)


