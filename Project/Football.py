# Erfan Rafiei Oskouei - 98243027

# Import libraries
import sqlite3

# Create a connection to a SQLite database file
conn = sqlite3.connect("database.sqlite")

# Create a cursor object to execute queries
cur = conn.cursor()

# Question 1: Retrieve the names of the tables in the database
cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cur.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])


print()
print("----------------------------------------")
print()

# Question 2: Retrieve the list of countries
cur.execute("SELECT DISTINCT * FROM Country")
countries = cur.fetchall()
print("Countries:")
for country in countries:
    print(country[0]," - ",country[1])

print()
print("----------------------------------------")
print()

# Question 3: Retrieve the list of leagues and their countries
cur.execute("SELECT DISTINCT * FROM League")
leagues = cur.fetchall()
print("Leagues and Countries:")
for league in leagues:
    print(league[2])

print()
print("----------------------------------------")
print()

# Question 4: Retrieve the list of teams in alphabetical order
cur.execute("SELECT DISTINCT * FROM Team ORDER BY team_long_name")
teams = cur.fetchall()
print("Teams by alphabetical order:")
for team in teams:
    print(team[3])

print()
print("----------------------------------------")
print()

# Question 5: Retrieve the list of 20 matches played in Spain with their details
cur.execute("""SELECT league_id, home_team_goal, away_team_goal, date, season 
               FROM Match 
               WHERE country_id='21518'""")
matches = cur.fetchmany(20)
print("The first 20 Matches in Spain:")
print("League ID, Home Goal, Away Goal, Date, Season")
for match in matches:
    print(match)

print()
print("----------------------------------------")
print()

# # Question 6: Extract the country name, league name, season, number of unique home teams, average home team goals, average away team goals, average goal difference,
# average total goals and total goals for matches played in Spain, Germany, France, Italy and England in each league and season

cur.execute("""SELECT country_id, league_id, season,
               COUNT(DISTINCT home_team_api_id) AS num_home_teams,
               AVG(home_team_goal) AS avg_home_goal,
               AVG(away_team_goal) AS avg_away_goal,
               AVG(home_team_goal - away_team_goal) AS avg_goal_diff,
               AVG(home_team_goal + away_team_goal) AS avg_total_goal,
               SUM(home_team_goal + away_team_goal) AS total_goal
               FROM Match
               WHERE country_id='21518' OR country_id='1729' OR country_id='4769' OR country_id='10257' OR country_id='7809'
               GROUP BY country_id, league_id, season""")
stats = cur.fetchall()

print("Statistics for matches in Spain, Germany, France, Italy and England:")
for stat in stats:
    print(stat)
    

# Close the connection
conn.close()
