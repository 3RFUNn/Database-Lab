# Erfan Rafiei Oskouei - 98243027

# Import pandas and sqlite3 libraries
import pandas as pd
import sqlite3

# Connect to the population_data.db file
conn = sqlite3.connect("population_data.db")
print() 
# Check if the tables are sqlite_sequence and facts
tables = pd.read_sql("""SELECT name FROM sqlite_master WHERE type='table';""", conn)
if tables.equals(pd.DataFrame([["sqlite_sequence"], ["facts"]], columns=["name"])):
    # Query 1: Which country has the highest and lowest population?
    df1 = pd.read_sql("""SELECT name, population FROM facts WHERE name <> 'World' ORDER BY population DESC;""", conn)
    highest_pop = df1.iloc[0]
    lowest_pop = df1.iloc[-1]
    print(f"The country with the highest population is {highest_pop['name']} with {highest_pop['population']} people.")
    print(f"The country with the lowest population is {lowest_pop['name']} with {lowest_pop['population']} people.")

    print()
    print("----------------------------------------")
    print()

    # Query 2: Which country has experienced the highest population growth?
    df2 = pd.read_sql("""SELECT name, (population - population_growth) / population_growth * 100 AS growth_rate FROM facts WHERE name <> 'World' ORDER BY growth_rate DESC;""", conn)
    highest_growth = df2.iloc[0]
    print(f"The country with the highest population growth is {highest_growth['name']} with {highest_growth['growth_rate']:.2f}% increase.")

    print()
    print("----------------------------------------")
    print()

    # Query 3: Which country has the highest and lowest population density relative to area?
    df3 = pd.read_sql("""SELECT name, population / area AS density FROM facts WHERE name <> 'World' ORDER BY density DESC;""", conn)
    highest_density = df3.iloc[0]
    lowest_density = df3.iloc[-1]
    print(f"The country with the highest population density is {highest_density['name']} with {highest_density['density']:.2f} people per square kilometer.")
    print(f"The country with the lowest population density is {lowest_density['name']} with {lowest_density['density']:.2f} people per square kilometer.")
    
    print()
    print("----------------------------------------")
    print()

    # Query 4: What are the top 10 countries with the highest migration rate in order?
    df4 = pd.read_sql("""SELECT name, migration_rate FROM facts WHERE name <> 'World' ORDER BY migration_rate DESC LIMIT 10;""", conn)
    print("The top 10 countries with the highest migration rate are:")
    for i, row in df4.iterrows():
        print(f"{i+1}. {row['name']} with {row['migration_rate']:.2f}%")
    
    print()
    print("----------------------------------------")
    print()

    # Query 5: What are the top 5 countries with the highest birth rate to death rate ratio in order?
    df5 = pd.read_sql("""SELECT name, birth_rate / death_rate AS ratio FROM facts WHERE name <> 'World' ORDER BY ratio DESC LIMIT 5;""", conn)
    print("The top 5 countries with the highest birth rate to death rate ratio are:")
    for i, row in df5.iterrows():
        print(f"{i+1}. {row['name']} with {row['ratio']:.2f}")
    
    print()
    print("----------------------------------------")
    print()

    # Query 6: Is there a significant relationship between death rate and population growth? (Hint: use pearson correlation)
    df6 = pd.read_sql("""SELECT death_rate, (population - population_growth) / population_growth * 100 AS growth_rate FROM facts WHERE name <> 'World';""", conn)
    corr = df6.corr(method="pearson")
    print(f"The pearson correlation coefficient between death rate and population growth is {corr.iloc[0,1]:.2f}")
    if abs(corr.iloc[0,1]) >= 0.5:
        print("There is a strong relationship between death rate and population growth.")
    elif abs(corr.iloc[0,1]) >= 0.3:
        print("There is a moderate relationship between death rate and population growth.")
    else:
        print("There is a weak or no relationship between death rate and population growth.")
else:
    # Print an error message
    print("The tables in this database are not sqlite_sequence and facts.")
