from fastapi import APIRouter, HTTPException, status
from api.models import PlayerDb, PlayerIn, PlayerInCreate
from api.database import players

router = APIRouter(prefix='/players', tags=['players'])

@router.get('', response_model=list[PlayerIn])
def get_players():
    return players

@router.get('/{id}', response_model=PlayerDb)
def get_player(id: int):
    index = -1
    for i, p in enumerate(players):
        if p['id'] == id:
            index = i
            break
    if index == -1:
        raise HTTPException(detail="Player not found", status_code=404)
    return players[index]

@router.post('', status_code=status.HTTP_201_CREATED, response_model=PlayerIn)
def create_player(player_in: PlayerInCreate):
    new_id = len(players) + 1
    player = PlayerDb(id=new_id, name=player_in.name)
    players.append(player.dict())
    return player
