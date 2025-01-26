#What question to answer?
try:
    Question = int(input("Question number?"))

except ValueError:
    print("Invalid input. Please enter a number")
    Question = None

#Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

print("Question number", Question)

#Question 1
#create library
if Question == 1:
    RJ_characterlib = {
        "names" : ["Romeo", "Juliet", "Tybalt", "Lady Capulet", "Mercutio"],
        "Age" : [16, 13, 17, 37, 15]
    }

    #create dataframe
    RJ_characterDF = pd.DataFrame(RJ_characterlib)

    #dataframe output
    print(RJ_characterDF)

#Question 2
elif Question == 2:
    #integer list
    int_list = [0, 1, 2, 3, 4, 5, 6, 7]
    print("Position 4 is", int_list[3])

    #tuple
    tup_list = ("Big", "meaty", "claws!")
    print("tuple list is", tup_list)

    #Dictionary
    DNA_dict = {
        "A" : 3,
        "T" : 5,
        "G" : 10,
        "C" : 6
    }

    #sum of all bases
    print("Sum of all bases is: ", DNA_dict["A"] + DNA_dict["T"] + DNA_dict["G"] + DNA_dict["C"])

    #list of lists (of floats)
    floatlist = [
        [0.522, 0.332, 0.063],
        [0.448, 0.174, 0.863],
        [0.538, 0.549, 0.551],
        [0.615, 0.971, 0.028],
        [0.510, 0.363, 0.943],
        [0.090, 0.841, 0.424],
        [0.779, 0.421, 0.344],
        [0.858, 0.554, 0.758],
        [0.322, 0.422, 0.789],
        [0.898, 0.695, 0.597]
        ]
    print("List 6, position 3 is:", floatlist[5][2])

    #Array of floats
    float_list = [6.46, 4.10, 8.24, 0.95, 5.06, 1.28, 6.49, 0.07, 7.38, 2.01]
    float_array = np.array(float_list)

    print("float array position 1-4 is:", float_array[0:3])

    #pandas dataframe
    yearlib = {
        "Name" : ["Intercessor", "Warp Spider", "Fire Warrior", "Nob", "Mortarion", "Termagant", "Swooping Hawk", "Fuegan", "Land Raider Redeemer", "Defiler"],
        "Year of release" : [2020, 1994, 2000, 2018, 2017, 2023, 2000, 2024, 2000, 2003]
    }

    yeardf = pd.DataFrame(yearlib)
    print(yeardf.iloc[[8]])

#Question 3
elif Question == 3:
    Method = int(input("Which method?"))
    #Method 1
    if Method == 1:
        for x in range(200,301):
            print(x)

    #Method 2
    if Method == 2:
        x=0
        while x <= 300:
            if x >= 200:
                print(x)
            x = x+1

    #Method 3
    if Method == 3:
        numlist = list(range(0,400))
        print(numlist[200:301])

#Question 4
elif Question == 4:
    animals = ["tiger", "lion", "badger", "fox", "rabbit", "fish", "dog", "octopus"]

    #replace fish
    animals[animals.index("fish")] = "hippopotomus"

    #add another animal
    animals.append("eagle")

    #replace octopus
    animals[animals.index("octopus")] = "clownfish"

    print(animals)

#Question 5
elif Question == 5:
    mtcars = "https://raw.githubusercontent.com/Apress/mastering-ml-w-python-in-six-steps/refs/heads/master/Chapter_2_Code/Data/mtcars.csv"
    cars = pd.read_csv(mtcars)
    #print(cars)
    cars.plot.scatter(x = 'mpg', y = 'hp')
    plt.show()

#Question 6
elif Question == 6:
    starwars_dataset = "https://www.fabricionarcizo.com/post/starwars/updated_starwars.csv"
    starwars = pd.read_csv(starwars_dataset)
    maxheight = starwars[
        starwars['height'].eq(starwars['height'].max())
    ][['name', 'height', 'films']]

    maxmass = starwars[
        starwars['mass'].eq(starwars['mass'].max())
    ][['name', 'mass', 'films']]

    print(maxheight.to_markdown())
    print(maxmass.to_markdown())

#Question 7
elif Question == 7:
    life_expectancy = sns.load_dataset("healthexp")

    #number of countries
    print("Total number of unique countries:", life_expectancy["Country"].nunique())

    #country with highest life expectancy
    life_country_grouped = life_expectancy.groupby("Country").mean()
    Country_Life_exp = life_country_grouped.sort_values("Life_Expectancy", ascending = False)
    Life_country = Country_Life_exp[["Life_Expectancy"]]
    print("Country with highest mean life expectancy")
    print(Life_country.head(1))

    #year with highest life expectancy
    Life_year = life_expectancy[["Year", "Life_Expectancy"]]
    Life_year_group = Life_year.groupby("Year").mean()
    Year_Life_exp = Life_year_group.sort_values("Life_Expectancy", ascending = False)
    print("Year with highest mean life expectancy")
    print(Year_Life_exp.head(1))

    #year with highest expenditure
    Expense_Life_crop = life_expectancy[["Year", "Spending_USD"]]
    Expense_year_group = Expense_Life_crop.groupby("Year").mean()
    Expense_Life_exp = Expense_year_group.sort_values("Spending_USD", ascending = False)
    print("Year with highest mean expenditure:")
    print(Expense_Life_exp.head(1))

    Expense_year_group = Expense_Life_crop.groupby("Year").sum()
    Expense_Life_exp = Expense_year_group.sort_values("Spending_USD", ascending=False)
    print("Year with highest total expenditure:")
    print(Expense_Life_exp.head(1))

# Question 8
elif Question == 8:
    diamonds = sns.load_dataset("diamonds")
    Graphtype = input("Which graph to see? (S=Scatter of carat vs price, H=Histogram of price, B=Boxplot of cut vs price): ").strip().upper()

    if Graphtype == "S":
        # Scatter plot Carat vs Price
        plt.scatter(x=diamonds["carat"], y=diamonds["price"], s=0.75)
        plt.xlabel("Carat")
        plt.ylabel("Diamond Price")
        plt.show()

    elif Graphtype == "H":
        # Histogram of prices
        plt.hist(diamonds["price"], bins=30)
        plt.xlabel("Price")
        plt.ylabel("Frequency")
        plt.show()

    elif Graphtype == "B":
        # Boxplot of cut vs price
        sns.boxplot(x="cut", y="price", data=diamonds)
        plt.xlabel("Cut")
        plt.ylabel("Price")
        plt.show()

    else:
        print("Invalid graph type selected.")



elif Question == 9:
    diamonds = sns.load_dataset("diamonds")

    dia_cost_low = diamonds.sort_values(by = "price", ascending = True)

    cheapest_diamond = dia_cost_low.iloc[0]["price"]

    print("Cheapest diamond: £", cheapest_diamond)


    dia_cost_high = diamonds.sort_values(by = "price", ascending = False)

    expensive_diamond = dia_cost_high.iloc[0]["price"]

    print("Most expensive diamond:", expensive_diamond)



elif Question == 10:
    diamonds = sns.load_dataset("diamonds")

    diamonds["weight_g"] = diamonds["carat"] * 0.2

    dia_sort_carat = diamonds.sort_values(by = "weight_g", ascending = False)

    heaviest_diamond_weight = dia_sort_carat.iloc[0]["weight_g"]

    print("The heaviest diamond is: ", heaviest_diamond_weight, " grams")

else:
    print("Invalid question number")