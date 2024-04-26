# Tuodaan moduulit
from pydantic import BaseModel
from typing import List

# Määritellään pelaaja
class PlayerIn(BaseModel):
    # Pelaajan nimi, odotetaan merkkijonoa.
    name: str
    # Pelaajan tunnus, odotetaan kokonaislukua.
    id: int

# Määritellään tapahtuma
class EventIn(BaseModel):
    # Tapahtuman tyyppi, odotetaan merkkijonoa.
    type: str
    # Lisätietoja tapahtumasta, odotetaan merkkijonoa.
    detail: str
    # Tapauksen aikaleima, odotetaan merkkijonoa.
    timestamp: str
    # Tapahtuman tunnus, odotetaan kokonaislukua.
    id: int

# Määritellään uusi tapahtuma
class EventInCreate(BaseModel):
    # Tapahtuman tyyppi, odotetaan merkkijonoa.
    type: str
    # Lisätietoja tapahtumasta, odotetaan merkkijonoa.
    detail: str

# Määritellään tapahtuman tietokantamalli
class EventDb(EventIn):
    # Pelaajan tunnus, odotetaan kokonaislukua.
    player_id: int

# Määritellään uuden pelaajan malli
class PlayerInCreate(BaseModel):
    # Pelaajan nimi, odotetaan merkkijonoa.
    name: str

# Määritellään pelaajan tietokantamalli
class PlayerDb(PlayerIn):
    # Lista pelaajan tapahtumista, oletusarvoisesti tyhjä.
    events: List[EventDb] = []
