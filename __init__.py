from db_handler import PickleDBHandler
from flask import Flask
import json

with open("questions_and_choices.json", "r", encoding="utf-8") as f:
    questions_and_choices_dictionary = json.load(f)

app = Flask(__name__, template_folder="templates", static_folder="static")

db_handler = PickleDBHandler("db.db")
