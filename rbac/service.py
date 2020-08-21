from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from utils import *

db_engine = create_engine('sqlite:///rbac', echo = True)

Session = sessionmaker(ddwqbind=db_engine)
Base.metadata.create_all(db_engine)

insert_into_user_table()
insert_into_action_table()
insert_into_userActionMap_table()
checkUserAuthentication(1, 1)