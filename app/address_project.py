
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

# SQLite database URL
sql_address = "sqlite:///./address.db"

# Create database engine
engine = create_engine(sql_address)

# Create a session factory for database operations
local_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for SQLAlchemy models
class Base(DeclarativeBase):
    pass

# Users table model
class users(Base):
    __tablename__ = "user_data"
    # Primary key column
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(30))
    user_password = Column(String(15))
    user_age = Column(Integer)

    def __repr__(self):
        return f"\nid={self.user_id},name={self.user_name},password={self.user_password},age={self.user_age}\n"

# Address table model
class address(Base):
    __tablename__ = "addresses"
    # Primary key column
    id = Column(Integer, primary_key=True, autoincrement=True)
    # Foreign key: it must use the table name, not the class name
    users_id = Column(Integer,ForeignKey("user_data.user_id"))
    city = Column(String(50))
    # Create relationship between address and users tables
    user = relationship("users")

    def __repr__(self):
        return f"\nid={self.id},user_id={self.user_id},city={self.city}\n"

# Create tables in the database
Base.metadata.create_all(engine)

# Create a database session
session = local_session()

# Find the first address where city is Shiraz
# The relationship allows accessing user information from the address object
user_address = session.query(address).where(address.city=="Shiraz").first()

# Access user_name from the related users table
print(user_address.user.user_name)