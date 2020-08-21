import logging

from sqlalchemy import create_engine
from models import *
# from service import db_engine

from sqlalchemy.orm import sessionmaker

db_engine = create_engine('sqlite:///rbac', echo = True)
Session = sessionmaker(bind = db_engine)
session = Session()

# def insert_into_country_table():
# 	session.add_all([
# 	   Customers(name = 'India', code = 91), 
# 	   Customers(name = 'US',code = 1),]
# 	)

# 	session.commit()


def insert_into_user_table():
	session.add_all([
	   CitiUser(name = 'Komal Pande'), 
	   CitiUser(name = 'Rajender Nath'), 
	   CitiUser(name = 'S.M.Krishna')]
	)

	session.commit()

	users = session.query(CitiUser).all()

	for user in users:
		print(user.name)

def insert_into_action_table():
	session.add_all([
	   Action(name = 'DBF'), 
	   Action(name = 'Pernum'), 
	   Action(name = 'CB')]
	)

	session.commit()

	actions = session.query(Action).all()

	for act in actions:
		print(act.name)


def insert_into_userActionMap_table():
	session.add_all([
	   CitiUserActionMap(user_id = 1, action_id = 1), 
	   CitiUserActionMap(user_id = 2, action_id = 2)]
	)

	session.commit()


def checkUserAuthentication(user_id, action_id):
	user_act_obj = session.query(CitiUserActionMap).\
							filter(CitiUserActionMap.user_id==user_id,
								CitiUserActionMap.action_id==action_id).first()
	if user_act_obj:
		print("User can take action\n\n\n")
	else:
		print("user is not allowed to take action\n\n\n")

