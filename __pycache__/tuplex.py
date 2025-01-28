weeks=[]
for i in range(1,7+1):
    week=str(input(f"Enter weeks  {i}:"))
    weeks.append(week)
weeks=tuple(weeks)
print("Weeks are",weeks)