from sqlalchemy.orm import Session
import schemas as schemas
from models import User, DiscountModel


def get_user(db: Session, bridge_id: str, authentication_token: str):
    user = db.query(schemas.User).filter(
        schemas.User.bridge_id == bridge_id,
        schemas.User.authentication_token == authentication_token
    ).first()
    return user


def get_device(db: Session, bridge_id: str, token: str):
    device_id = db.query(schemas.User).filter(
        schemas.User.authentication_token == token,
        schemas.User.bridge_id == bridge_id
    ).first()
    return device_id.machine_id if device_id else None


def create_user(db: Session, user: User):
    db_user = schemas.User(bridge_id=user.bridge_id, authentication_token=user.authentication_token)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def create_auth(db: Session, user: Auth):
#     db_user = schemas.Auth(username=user.username, password=user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def add_discount(db: Session,
                 company_name: str,
                 discount_price,
                 discount_percentage,
                 discount_product_name,
                 discount_url, timestamp):
    discount = schemas.Discount(
        name_of_company=company_name,
        discount_percentage=discount_percentage,
        discount_price=discount_price,
        discount_product=discount_product_name,
        discount_url=discount_url,
        discount_timestamp=timestamp
    )

    db.add(discount)
    db.commit()
    return discount
