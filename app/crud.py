from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models

def get_nearest_sequence(db: Session, x: float, y: float):
    # Calcular la distancia cuadrada y ordenar por la más cercana
    nearest = db.query(
        models.Sequence,
        func.sqrt(func.pow(models.Sequence.x - x, 2) + func.pow(models.Sequence.y - y, 2)).label('distance')
    ).order_by('distance').first()
    
    if nearest:
        return {
            "sequence": nearest.Sequence.sequence,
            "distance": nearest.distance,
            "descripcion": nearest.Sequence.descripcion,
            "mru": nearest.Sequence.mru
        }
    else:
        return None
