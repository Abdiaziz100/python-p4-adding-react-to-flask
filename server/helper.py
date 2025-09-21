# server/helper.py

def serialize(model):
    """
    Converts a SQLAlchemy model instance into a dictionary.
    Each column becomes a key-value pair in the dictionary.
    """
    return {c.name: getattr(model, c.name) for c in model.__table__.columns}
