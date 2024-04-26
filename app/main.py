from fastapi import FastAPI
from endpoints import players, events

app = FastAPI()

app.include_router(players.router)
app.include_router(events.router)
