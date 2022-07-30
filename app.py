teams = ["Human", "Dragon", "Slave", "Unicorn", "Orc", "Magician", "Fruit Slayer"]

for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)


friends = ["Rivano" , "Fauzan", "Hazlan", "Cemilik", "Gilang", "Bintang", "Mas Pram", "Najma", "Julio", "Regularity", "Singularity"]

for friend in friends:
    print("Hi " + friend)


for i in range(10):
    print("Hello, World!")

for i in range(5):
  print("This is fun!")

seconds_in_a_day = 86400
seconds_in_a_week = seconds_in_a_day*7
print(seconds_in_a_week)

base = 5
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))

bill = 47.28
tip = bill * (0.15)
total = bill + tip
share = total / 2 
print("Each person needs to pay: " + str(share))