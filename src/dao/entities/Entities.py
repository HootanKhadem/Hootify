from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

db_name = "Hootify"
base = declarative_base()

role_person_association_table = Table('person_role', base.metadata,
                                      Column('person_id', Integer, ForeignKey('persons.id')),
                                      Column('role_id', Integer, ForeignKey('role.id')))


class Movie(base):
    def __init__(self, movie_name=None, year=None, db_id=None):
        self.db_id = db_id
        self.movie_name = movie_name
        self.year = year

    __tablename__ = "movies"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    movie_name = Column('movie_name', String(255), nullable=False)
    year = Column('year', Integer, nullable=False)
    kind = Column('kind', String(255))

    def get_object_name(self):
        return self.movie_name


class Person(base):
    def __init__(self, db_id=None, first_name=None, last_name=None, role=list()):
        self.id = db_id
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    __tablename__ = "persons"

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    first_name = Column('first_name', String(255), nullable=False)
    last_name = Column('last_name', String(255), nullable=False)
    role = relationship("Role",
                        secondary=role_person_association_table)

    def get_object_name(self):
        return self.first_name + " " + self.last_name


class Role(base):
    def __init__(self, name=None, db_id=None):
        self.id = db_id
        self.name = name

    __tablename__ = "role"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(255), nullable=False)

    def get_object_name(self):
        return self.name


class PersonMovieRelation(base):
    def __init__(self, person_id=None, movie_id=None, role_id=None):
        self.person_id = person_id
        self.movie_id = movie_id
        self.role_id = role_id

    __tablename__ = "person_movie"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    person_id = Column('person_id', Integer)
    movie_id = Column('movie_id', Integer)
    role_id = Column('role_id', Integer)

    def set_role_id(self, role_id):
        self.role_id = role_id

    def set_person_id(self, person_id):
        self.person_id = person_id


def create_database():
    engine = create_engine('mysql://root:123@localhost/' + db_name, echo=True)
    base.metadata.create_all(bind=engine)
