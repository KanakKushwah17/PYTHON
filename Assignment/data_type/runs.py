"""
Assignment 7: Cricket Run Rate

In cricket, overs are given in decimal format (e.g., 48.3 means 48 overs and 3 balls). Convert overs into total balls and calculate run rate.

Input:
Total runs = 275
Overs = 48.3

Expected Output:
Total Balls = 291
Run Rate = 5.67
"""
Totalruns=int(input("Enter the runs :"))
Overs= float(input("Enter the Overs :"))
ball=Overs%10
Over=Overs//10
Totalballs=(Over*6)+ball
print(Totalballs)
runrate=float(Totalruns/Overs)
print("Run rate :",runrate)


