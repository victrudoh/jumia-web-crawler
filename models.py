from pydantic import BaseModel


class User(BaseModel):
    authentication_token: str
    bridge_id: str


class AuthModel(BaseModel):
    username: str
    password: str


class DiscountModel(BaseModel):
    name_of_company: str
    discount_name: str
    discount_price: str
    discount_product: str
    discount_url: str
    discount_timestamp: str
