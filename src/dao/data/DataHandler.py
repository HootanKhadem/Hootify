from src.dao.entities.Entities import Movie, Person, Role, PersonMovieRelation
from src.dao.database import DB as DATABASE
from src.controller.Main import Methods as methods


class DataHandler:
    data = []
    required_roles = ['directors', 'cast']

    def __init__(self, data):
        self.data = data

    def create_movie_object(self):
        new_movie = Movie()
        new_movie.year = self.data['year']
        new_movie.kind = self.data['kind']
        new_movie.movie_name = self.data['title']
        try:
            inserted_movie_id = DATABASE.insert_object(new_movie)
            return inserted_movie_id
        except:
            return new_movie.movie_name + "Not inserted"

    def create_person_and_relations(self, movie_id):
        persons = []
        for role in self.required_roles:
            person_with_role_array = self.data[role]
            acquired_role = self.get_role(role)
            for person in person_with_role_array:
                first_name, last_name = methods.get_person_name(person)
                person_found = DATABASE.select_person_object(first_name, last_name)
                if len(person_found) == 0:
                    new_person = Person(first_name=first_name, last_name=last_name)
                    new_person.role.append(acquired_role)
                    role_id = DATABASE.insert_object(acquired_role)
                    new_person.id = DATABASE.insert_object(new_person)
                    persons.append(new_person)
                    person_movie_relation = PersonMovieRelation(movie_id=movie_id, person_id=new_person.id,
                                                                role_id=role_id)
                    self.create_person_movie_relation(person_movie_relation)
                else:
                    for existing_person in person_found:
                        persons.append(existing_person)
        return persons

    def get_role(self, role_name):
        role_found = DATABASE.select_role(role_name)
        if len(role_found) is not 0:
            return role_found[0]
        new_role = Role()
        new_role.name = role_name
        return new_role

    def bind_data(self):
        movie_exists = self.check_for_movie()
        if not movie_exists:
            movie_id = self.create_movie_object()
            self.create_person_and_relations(movie_id)
        return {"movie_title": self.data['title'], "directors_name": self.data['directors'], "kind": self.data['kind']}

    def check_for_movie(self):
        movie_found = DATABASE.select_movies(self.data['title'], self.data['year'])
        if len(movie_found) > 0:
            return True
        return False

    def create_person_movie_relation(self, _object):
        DATABASE.insert_object(_object)

    def get_movie_count(self, roles):
        for role_name in roles:
            role_id = DATABASE.get_role_id(role_name)
            movie_id = DATABASE.get_movie_id(movie_name=self.data['title'], movie_year=self.data['year'])
            director_id = DATABASE.get_director_id(movie_id=movie_id, role_id=role_id)
            a = DATABASE.get_count_from_person_movie(role_id=role_id, person_id=director_id)
            return 1
