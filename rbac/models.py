from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.types import Date
from sqlalchemy.types import DateTime
from datetime import datetime

Base = declarative_base()

class Action(Base):
	__tablename__ = 'Action'
	id = Column(Integer, primary_key=True)
	name = Column(String, nullable = False)
	created_on = Column(DateTime(), default=datetime.now)
	updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return "<Action(action_name='%s')>" % (self.name)




class CitiUser(Base):
	__tablename__ = 'CitiUser'
	id = Column(Integer, primary_key=True)

	# title = Column(String)
	name = Column(String, nullable = False)
	# middle_name = Column(String)
	# last_name = Column(String, nullable = False)
	# gender = Column(String, nullable = False)
	# email = Column(String, nullable = False)
	# dob = Column(Date(), nullable = False)
	# # has_role = Column(Boolean, default = False)
	# status = Column(Integer, default = 1) #0 deactivated, 1 active,  2 blocked 
	# country_id = Column(Integer, ForeignKey('Country.id', ondelete='CASCADE'), nullable = False)
	created_on = Column(DateTime(), default=datetime.now)
	updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


	def __repr__(self):
		return "<User(first_name='%s', middle_name='%s', last_name='%s', country='%s')>" \
							% (self.first_name, self.middle_name, self.middle_name, self.country)



class CitiUserActionMap(Base):
	__tablename__ = 'CitiUserActionMap'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('CitiUser.id', ondelete='CASCADE'), nullable = False)
	action_id = Column(Integer, ForeignKey('Action.id', ondelete='CASCADE'), nullable = False)
	created_on = Column(DateTime(), default=datetime.now)
	updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


