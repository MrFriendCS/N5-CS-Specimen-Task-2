# Title: N5 CS Specimen Task 2
# Author: Mr Friend
# Date: 19 Feb 2022

# Initialise variables
playerHits = 0
teamHits = [0] * 6
totalHits = 0
averageHits = 0.0
points = 0

#  Get 6 valid hits from players
for index in range(6):
    playerHits = int(input(str(index + 1) + ". How many hits? "))

    while playerHits < 0 or playerHits > 30:
        print("Hits must be from 0 to 30")
        playerHits = int(input(str(index + 1) + ". How many hits? "))
    
    teamHits[index] = playerHits

# Calculate total hits for 6 players
for index in range(6):
    totalHits = totalHits + teamHits[index]

# Calculate average hits
averageHits = totalHits / 6

# Round average hits to 2 decimal places
averageHits = round(averageHits, 2)

print("The average hits are: " + str(averageHits))

# Calculate points earned
if totalHits > 50:
    points = points + 1

if averageHits >= 10:
    points = points + 1

# 1 point earned?
if points >= 1:
    # Yes - display message - 1 point was earned
    print("1 point was earned")

# 2 points earned?
if points == 2:
    # Yes - display message - additional point was earned
    print("An additional point was earned")

# 0 points earned?
if points == 0:
    # Yes - display message - no points were earned
    print("No points were earned")

# End