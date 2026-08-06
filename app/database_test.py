
from sqlalchemy import create_engine # create engine is for make a connection to database
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import Mapped,mapped_column # important!: these tow module are check the type strictly
from sqlalchemy.orm import sessionmaker # sessionmaker can make session(session is like cursor)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import or_,and_,not_ # these are for where method

sql_address = "sqlite:///./first_database.db" # address of database :)

# engine is connection between this file and database
engine = create_engine(sql_address,connect_args={"check_same_thread":False})
# line 9 of this code (connect_args={check_same_thread:False}) allow the program to do many works at the same time
# your can't change connect_args to different variable

# this line is for creating session (cursor)
local_session = sessionmaker(autocommit=False, # this line say if I don't say commit the code can't commit the progress
                       autoflush=False, # this line is like autocommit but in large scale
                       bind=engine)

class Base(DeclarativeBase): # in here we create one base class for tables
    pass

# --------------------Create Tables--------------------
# for create table we should create one class
# for datatype and columns we should import them from sqlalchemy (see line 3)

# in this class we didn't check the type of variables strictly
class user(Base):
    __tablename__ = "users" # important!: in here we choose the table name
    user_id = Column(Integer,primary_key=True,autoincrement=True)
    user_name = Column(String(30)) # this number is the maximum length of input
    age = Column(Integer,nullable=True)

    def __repr__(self):
        """
        this function is for change the type of out put:
        if output is this ==> <__main__.User object at 0x7f...>
        it change it to this one ==> User(id = {1},name = {Amir},age = {16})
        """
        return f"User(id = {self.user_id},name = {self.user_name},age = {self.age})"

# in this class we checked the type of variables strictly
class users_2(Base):
    __tablename__ = "user_2" # table name = user_2
    # in user_age line nullable mean it can be null at first of inserting
    user_id : Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    user_name : Mapped[str] = mapped_column(String(30))
    user_age : Mapped[int] = mapped_column(Integer,nullable=True)

    def __repr__(self):
        return f"User_2(id = {self.user_id},name = {self.user_name},age = {self.user_name})"

# ---------------------- Run line ---------------------
Base.metadata.create_all(engine) # this line create tables

# ---------------------- add data ---------------------
# for adding data first we should make one session
session = local_session() # local session is in line 16
# after this we have add method so at first we should create an variable

# person_1 = user(user_name="Amir",age=16)
# session.add(person_1)
# session.commit()

# we should commit here because we change the setting of autocommit
# now me add one item to database

# another adding to database:

# person_2 = user(user_name="Daniel",age=16)
# session.add(person_2)
# session.commit()

# ---------- add a list of data ----------
# person_3 = user(user_name="Arnoosh",age=17)
# person_4 = user(user_name="Pooria",age=17)
# users_list = [person_3,person_4]
# session.add_all(users_list)
# session.commit()

# ------------- retrieve data -------------
# if repr function doesn't exist data can't readable
users = session.query(user).all()
print(users)

# let's use filter for fetching data

filter_user = session.query(user).filter_by(user_name="Amir").all()
print(filter_user)

filter_user2 = session.query(user).filter_by(age=16).all()
print(filter_user2)

# if we just want the first object:
filter_user3 = session.query(user).filter_by(age=16).first()
print(filter_user3)

# if we want one of the data
# Important: if there is more than one row in the database matching the filter, one_or_none() raises an error.
filter_user4 = session.query(user).filter_by(user_name="Amir").one_or_none()
print(filter_user4)

# ------------- update data -------------
# for updating data first we should find it in database
# then change where we want

user_data1 = session.query(user).filter_by(user_name="Arnoosh",age=17).one_or_none()
try:
    user_data1.age = 18
    session.commit()
except:
    print(user_data1)
print(session.query(user).all())

# ------------- deleting data -------------

user_delete1 = session.query(user).filter_by(user_name="Pooria").one_or_none()
try:
    session.delete(user_delete1)
    session.commit()
except:
    print(user_delete1)
print(session.query(user).all())

# ------------- filters and conditions -------------
# when we want to use >= or <= in filter we should use table name
user_filter1 = session.query(user).filter(user.age<=17).all()
print(user_filter1)
# or we can use where
user_filter2 = session.query(user).where(user.age<=17).all()
print(user_filter2)