
from base import Session, engine, Base

from client import Client
from sqlalchemy import update, Column, String

def generete_database_schema():
    Base.metadata.create_all(engine)
    
session = Session()

def commit_():
    session.commit()
    session.close()
    
    
def client():
    castorama = Client('Castorama')
    vw = Client('VW')
    boss = Client('Boss')
    
    session.add(castorama)
    session.add(vw)
    session.add(boss)

    
# clients = session.query(Client).all()
#
# # for client in clients:
# #     print(client.id)
# #     print(client.name)
# # v1 = Column('name', String)
# dic_ = {'name': 'Nowy 100'}
# stm = update(Client).where(Client.id == 3).values(**dic_)
# engine.execute(stm)


if __name__=="__main__":
    generete_database_schema()
    client()
    commit_()