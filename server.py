from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/check_ticket")
def check_ticket(data: dict):
    game = data["game"]
    numbers = data["numbers"]

    # Aquí placeholder de números ganadores
    winning_numbers = [1,2,3,4,5,6]  

    matched = len(set(numbers) & set(winning_numbers))
    prize = matched * 10  # demo

    return {
        "game": game,
        "matched": matched,
        "prize": prize,
        "winning_numbers": winning_numbers
    }
