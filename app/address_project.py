
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

sql_address = "sqlite:///./address.db"
engine = create_engine(sql_address)

local_session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

class Base(DeclarativeBase):
    pass

class users(Base):
    __tablename__ = "user_data"
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(30))
    user_password = Column(String(15))
    user_age = Column(Integer)

    def __repr__(self):
        return f"\nid={self.user_id},name={self.user_name},password={self.user_password},age={self.user_age}\n"

class address(Base):
    __tablename__ = "addresses"
    id = Column(Integer,primary_key=True,autoincrement=True)
    users_id = Column(Integer,ForeignKey("user_data.user_id")) # it must me the table name not the class name
    city = Column(String(50))
    user = relationship("users")

    def __repr__(self):
        return f"\nid={self.id},user_id={self.user_id},city={self.city}\n"

Base.metadata.create_all(engine)
session = local_session()

# here the relationship help us to find user_name from users class with address class
user_address = session.query(address).where(address.city=="Shiraz").first()
print(user_address.user.user_name)