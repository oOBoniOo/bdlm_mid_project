from pymongo import MongoClient

client = MongoClient()
db = client.get_database("euro_2020")
matchs = db.matchs
players = db.players
teams = db.teams
squads = db.squads