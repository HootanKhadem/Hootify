from sqlalchemy.orm import Session, sessionmaker

from src.dao.entities import Entities as entity

from sqlalchemy import create_engine as create_engine, select
from sqlalchemy.ext.declarative import declarative_base
import mysql.connector

from src.dao.entities.Entities import Person, Role, Movie

db_name = "Hootify"
base = declarative_base()
engine = create_engine('mysql://root:123@localhost/', echo=True)
check_db_query = "CREATE DATABASE IF NOT EXISTS Hootify;"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123",
    database="Hootify"
)


def create_database_and_tables(self):
    print("Creating database")
    engine.execute(check_db_query)
    self.engine = create_engine('mysql://root:123@localhost/Hootify', echo=True)
    entity.create_database()


def insert_object(_object):
    database_session = get_new_session()
    try:
        database_session.add(_object)
    except:
        _object_name = _object.get_object_name()
        print("Could not add " + _object_name)
    database_session.commit()
    object_id = _object.id
    database_session.close()
    return object_id


def select_person_object(first_name, last_name):
    session = get_new_session()
    result = session.query(Person).filter(Person.first_name == first_name, Person.last_name == last_name).all()
    session.close()
    return result


def select_movies(movie_name, movie_year):
    session = get_new_session()
    result = session.query(Movie).filter(Movie.movie_name == movie_name, Movie.year == movie_year).all()
    session.close()
    return result


def get_movie_id(movie_name, movie_year):
    session = get_new_session()
    result = session.query(Movie.id).filter(Movie.movie_name == movie_name, Movie.year == movie_year).all()
    session.close()
    return result


def select_role(role_name):
    session = get_new_session()
    result = session.query(Role).filter(Role.name == role_name).all()
    session.close()
    return result


def get_role_id(role_name):
    session = get_new_session()
    result = session.query(Role.id).filter(Role.name == role_name).all()
    session.close()
    return result


#
# def director_folder(director_name):
#     session = get_new_session()
#     result = session.statement.with_only_columns([func.count()])


def get_new_session():
    session = Session()
    session.bind = engine
    return session


def get_count_from_person_movie(role_id, person_id):
    query = "SELECT COUNT(*) FROM person_movie pm WHERE pm.role_id = " + str(role_id) \
            + " AND pm.person_id = " + str(person_id)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def get_director_id(movie_id, role_id):
    query = "SELECT pm.person_id FROM person_movie pm WHERE pm.role_id = " + str(role_id) \
            + " AND pm.movie_id = " + str(movie_id)
    mycursor = mydb.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()
