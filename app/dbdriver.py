from sqlalchemy import create_engine, Table, Column, Integer, MetaData, JSON
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from queue import Queue
from threading import Thread
import json
# QUEUE to add to db
q = Queue()


# from flask routs func
def add_repos_to_db(request_json):
    q.put(request_json)


metadata = MetaData()

# table for repos
repos_table = Table('repos_table', metadata,
    Column('id', Integer, primary_key=True),
    Column('repos', JSON)
)


# object for ORM
class ReposObj(object):
    def __init__(self, repos):
        self.repos = repos


mapper(ReposObj, repos_table)

# My sqlite db
engine = create_engine('sqlite:///repos_db.db', echo=True)
# add table to db
metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine, autocommit=True, autoflush=True)
session = Session()


""" thread for working with db, add repos to db from queue in this case"""
def insert_to_db_thread():
    while True:
        request_list = json.loads(q.get())
        session.add_all(map(lambda repos: ReposObj(json.dumps(repos)), request_list))



# thread start
Thread(target=insert_to_db_thread, daemon=True).start()
