
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy import String,Integer,Text,Column

sql_address = "sqlite:///./user_profile.db"
engine = create_engine(sql_address)

local_session = sessionmaker(autoflush=False,autocommit=False,bind=engine)

class Base(DeclarativeBase):
    pass

class users(Base):
    __tablename__ = "users"
    id = Column(Integer,autoincrement=True,primary_key=True)
    user_name = Column(String(30))
    password = Column(String(15))

    def __repr__(self):
        return f"\nid = {self.id},user_name = {self.user_name},password = {self.password}\n"

class profile(Base):
    __tablename__ = "profile"
    id = Column(Integer,primary_key=True,autoincrement=True)
    # in user_id, unique is because every user can only have one profile
    user_id = Column(Integer,ForeignKey("users.id"),unique=True)
    first_name = Column(String(30))
    last_name = Column(String(30))
    national_id = Column(Integer)
    bio = Column(Text,nullable=True)

    def __repr__(self):
        return f"\nuser id = {self.user_id},first name = {self.first_name},last name = {self.last_name},national id = {self.national_id},bio = {self.bio}\n"

Base.metadata.create_all(engine)

session = local_session()
