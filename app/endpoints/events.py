# Tuodaan tarvittavat toiminnot ja luokat muista tiedostoista
from endpoints.players import get_player 
from api.models import EventDb, EventInCreate  
from fastapi import APIRouter, HTTPException, status  
from datetime import datetime  
from re import match  
from api.database import types, events  

# Luodaan APIRouter-olio, joka käyttää /players-polkua ja merkitään tag 'players'
router = APIRouter(prefix='', tags=['players'])

# Endpoint pelaajan kaikkien eventtien hakemiseksi
@router.get('/players/{id}/events', response_model=list[EventDb])
def get_events(id: int, type: str = None):
    # Tarkistetaan, että annettu eventin tyyppi on kelvollinen
    if type is not None and type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    # Haetaan pelaajan tiedot
    player = get_player(id)
    # Muunnetaan pelaajan eventit sanakirjalistaksi
    player_events = [dict(event) for event in player['events']]

    # Suodatetaan eventit, jos annettu eventin tyyppi
    if type:
        filtered_events = [
            event for event in player_events if event['type'] == type]
    else:
        filtered_events = player_events

    return filtered_events

# Endpoint uuden eventin luomiseksi pelaajalle
@router.post('/players/{id}/events', status_code=status.HTTP_201_CREATED, response_model=EventDb)
def create_events(id: int, event_in: EventInCreate):
    # Haetaan pelaajan tiedot
    player = get_player(id)

    # Tarkistetaan, että annettu eventin tyyppi on kelvollinen
    if event_in.type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    # Luodaan uusi eventti
    new_id = len(events) + 1
    event = EventDb(
        id=new_id, type=event_in.type, detail=event_in.detail,
        timestamp=datetime.now().strftime('%Y-%m-%d, %H:%M:%S'), player_id=id
    )
    events.append(event.dict())
    player['events'].append(event)

    return event

# Endpoint kaikkien eventtien hakemiseksi
@router.get('/events', response_model=list[EventDb])
def get_events(type: str = None):
    # Tarkistetaan, että annettu eventin tyyppi on kelvollinen
    if type is not None and type not in types:
        raise HTTPException(status_code=400, detail="Invalid event type")

    # Palautetaan kaikki eventit, jos eventin tyyppiä ei ole määritelty
    if type is None:
        return events

    # Suodatetaan eventit, jos annettu eventin tyyppi
    filtered_events = [event for event in events if event['type'] == type]
    return filtered_events
