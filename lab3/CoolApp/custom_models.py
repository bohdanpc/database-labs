#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
import json

class AbstractManager(object):


	def __init__(self, table_name, columns_list):
		self.__table_name = table_name
		self.__columns = columns_list


	def get_objects_where(self, condition):
		try:
			con = mdb.connect('localhost', 'root', '1234', 'mydb')
			cur = con.cursor(mdb.cursors.DictCursor)
			cur.execute("SELECT * FROM " + self.__table_name + " " + condition)
			return cur.fetchall()
		except mdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		finally:
			if con:
				con.close()


	def delete(self, condition):
		try:
			con = mdb.connect('localhost', 'root', '1234', 'mydb')
			cur = con.cursor()
			cur.execute("DELETE FROM " + self.__table_name + " " + condition)
			con.commit()
		except mdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		finally:
			if con:
				con.close()


	def insert(self, row):
		try:
			con = mdb.connect('localhost', 'root', '1234', 'mydb')
			cur = con.cursor()
			request = "INSERT INTO " + self.__table_name + "("
			values_part = "VALUES('"
			for column in self.__columns:
				request += column + ", " 
				values_part += str(row[column]) + "', '"

			request = request[:-2] + ") "
			values_part = values_part[:-3] + ")"
			request += values_part

			cur.execute(request)
			con.commit()
		except mdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		finally:
			if con:
				con.close()


	def insert_all(self, data):
		try:
			con = mdb.connect('localhost', 'root', '1234', 'mydb')
			cur = con.cursor()
			for row in data:
				request = "INSERT INTO " + self.__table_name + "("
				values_part = "VALUES('"
				for column in self.__columns:
					request += column + ", " 
					values_part += str(row[column]) + "', '"

				request = request[:-2] + ") "
				values_part = values_part[:-3] + ")"
				request += values_part
				cur.execute(request)

			con.commit()
		except mdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		finally:
			if con:
				con.close()


	def update(self, id, row):
		try:
			con = mdb.connect('localhost', 'root', '1234', 'mydb')
			cur = con.cursor()

			request = "UPDATE " + self.__table_name + " SET "

			for column in self.__columns:
				request += column + "= '" + str(row[column]) +  "', "

			request = request[:-2] + " WHERE id = " + str(id)

			cur.execute(request)
			con.commit()
		except mdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		finally:
			if con:
				con.close()


	def full_text_search(self, condition):
		try:
			con = mdb.connect('localhost', 'root', '1234', 'mydb')
			cur = con.cursor(mdb.cursors.DictCursor)
			cur.execute("SELECT * FROM " + self.__table_name + " " + condition)
			return cur.fetchall()
		except mdb.Error, e:
			print "Error %d: %s" % (e.args[0], e.args[1])
		finally:
			if con:
				con.close()


	def get_all(self):
		return self.get_objects_where("")


	def get_by_id(self, id):
		return self.get_objects_where("WHERE id = " + str(id))[0]


	def delete_all(self):
		self.delete("")


	def delete_by_id(self, id):
		self.delete("WHERE id = " + str(id))
	

class PersonsManager(AbstractManager):
	def __init__(self):
		columns = ["name", "surname", "middlename", "birthdate"]
		table_name = "CoolApp_person"
		super(PersonsManager, self).__init__(table_name, columns)


	def get_all(self):
		return super(PersonsManager, self).get_all()

	def get_by_id(self, id):
		return super(PersonsManager, self).get_by_id(id)

	def get_objects_where(self, condition):
		return [Person(x) for x in super(PersonsManager, self).get_objects_where(condition)]

	def get_choice_lst(self):
		return tuple(tuple([obj.id, obj.name + " " + obj.surname]) for obj in self.get_all())

	def full_text_search(self, condition):
		return [Person(x) for x in super(PersonsManager, self).full_text_search(condition)]
	

class DoctorsManager(AbstractManager):
	def __init__(self):
		columns = ["person_id", "hospital_id", "position", "experience"]
		table_name = "CoolApp_doctor"
		super(DoctorsManager, self).__init__(table_name, columns)
	def get_all(self):
		return super(DoctorsManager, self).get_all()
	def get_by_id(self, id):
		return super(DoctorsManager, self).get_by_id(id)
	def get_objects_where(self, condition):
		return [Doctor(x) for x in super(DoctorsManager, self).get_objects_where(condition)]
	def get_choice_lst(self):
		return tuple(tuple([obj.id, obj.person.name + " " + obj.person.surname]) for obj in self.get_all())
	def full_text_search(self, condition):
		return [Doctor(x) for x in super(DoctorsManager, self).full_text_search(condition)]


class HospitalsManager(AbstractManager):
	def __init__(self):
		columns = ["name", "city", "state", "street", "build_no"]
		table_name = "CoolApp_hospital"
		super(HospitalsManager, self).__init__(table_name, columns)
	def get_all(self):
		return super(HospitalsManager, self).get_all()
	def get_by_id(self, id):
		return super(HospitalsManager, self).get_by_id(id)
	def get_objects_where(self, condition):
		return [Hospital(x) for x in super(HospitalsManager, self).get_objects_where(condition)]
	def get_choice_lst(self):
		return tuple(tuple([obj.id, obj.name]) for obj in self.get_all())
	def full_text_search(self, condition):
		return [Hospital(x) for x in super(HospitalsManager, self).full_text_search(condition)]


class SurveysManager(AbstractManager):
	def __init__(self):
		columns = ["pacient_id", "doctor_id", "diagnosis", "closing_date"]
		table_name = "CoolApp_surveyresult"
		super(SurveysManager, self).__init__(table_name, columns)
	def get_all(self):
		return super(SurveysManager, self).get_all()
	def get_by_id(self, id):
		return super(SurveysManager, self).get_by_id(id)
	def get_objects_where(self, condition):
		return [SurveyResult(x) for x in super(SurveysManager, self).get_objects_where(condition)]
	def full_text_search(self, condition):
		return [SurveyResult(x) for x in super(SurveysManager, self).full_text_search(condition)]



class Person(object):
	fields = ["name", "surname", "middlename", "birthdate"]
	def __init__(self, obj_list):
		self.id = obj_list['id']
		self.name = obj_list['name']
		self.surname = obj_list['surname']
		self.middlename = obj_list['middlename']
		self.birthdate = obj_list['birthdate']
	def __str__(self):
		return (self.name + " " + self.surname).encode('utf8')


class Doctor(object):
	fields = ["person_id", "hospital_id", "position", "experience"]
	def __init__(self, attr_list):
		self.id = attr_list['id']
		self.person = ObjectsManager.get_persons_manager().get_by_id(attr_list['person_id'])
		self.hospital = ObjectsManager.get_hospitals_manager().get_by_id(attr_list['hospital_id'])
		self.position = attr_list['position']
		self.experience = attr_list['experience']
	def __str__(self):
		return str(self.person).encode('utf8')


class Hospital(object):
	fields = ["name", "city", "state", "street", "build_no"]
	def __init__(self, attr_list):
		self.id = attr_list['id']
		self.name = attr_list['name']
		self.city = attr_list['city']
		self.state = attr_list['state']
		self.street = attr_list['street']
		self.build_no = attr_list['build_no']
	def __str__(self):
		return self.name.encode('utf8')


class SurveyResult(object):
	fields = ["pacient_id", "doctor_id", "diagnosis", "closing_date"]
	def __init__(self, attr_list):
		self.id = attr_list['id']
		self.pacient = ObjectsManager.get_persons_manager().get_by_id(attr_list['pacient_id'])
		self.doctor = ObjectsManager.get_doctors_manager().get_by_id(attr_list['doctor_id'])
		self.diagnosis = attr_list["diagnosis"]
		self.closing_date = attr_list["closing_date"]
	def __str__(self):
		return ("Survey Result #" + str(self.id)).encode('utf8')


class ObjectsManager(object):
	persons = PersonsManager()
	doctors = DoctorsManager()
	hospitals = HospitalsManager()
	survey_results = SurveysManager()

	@classmethod
	def get_persons_manager(cls):
		return cls.persons

	@classmethod
	def get_doctors_manager(cls):
		return cls.doctors

	@classmethod
	def get_hospitals_manager(cls):
		return cls.hospitals

	@classmethod
	def get_surveys_manager(cls):
		return cls.survey_results


def load_data(filename):
	with open(filename) as datafile:
		data = json.load(datafile)
	return data


def get_current_path(request):
    return {
       'current_path': request.get_full_path()
     }


def create_procedure():
    try:
    	con = mdb.connect('localhost', 'root', '1234', 'mydb')
        with con:
            cur = con.cursor()
            cur.execute("CREATE PROCEDURE clearLog() BEGIN DELETE FROM CoolApp_personlog; END;")
            con.commit()

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])	
        sys.exit(1)
    finally:
        if con:
            con.close()


def create_event(minutes_to_wait):
    try:
    	con = mdb.connect('localhost', 'root', '1234', 'mydb')
        with con:

            cur = con.cursor()
            cur.execute('SET @@global.event_scheduler = ON;')
            cur.execute("CREATE EVENT logCleaner "
                         "ON SCHEDULE AT CURRENT_TIMESTAMP + INTERVAL %s MINUTE "
                         "DO CALL clearLog(); " % minutes_to_wait)
            con.commit()
            return 0



    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()



def create_person_trigger():
    try:
        con = mdb.connect('localhost', 'root', '1234', 'mydb')
        with con:
            cur = con.cursor()
            
            cur.execute("DROP TRIGGER IF EXISTS logger;")
            cur.execute(
                "CREATE TRIGGER logger "
                "BEFORE DELETE "
                "ON CoolApp_person FOR EACH ROW "
                "BEGIN "
                "INSERT INTO CoolApp_personlog"
                "(name, surname, delete_time) "
                "VALUES"
                "(OLD.name, OLD.surname, curdate()); "
                "END;")
            
    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()


def drop_trigger():
    try:
        con = mdb.connect('localhost', 'root', '1234', 'mydb')
        with con:
            cur = con.cursor()
            cur.execute("DROP TRIGGER IF EXISTS logger;")

    except mdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        if con:
            con.close()


def populate_tables():

    survey_data = load_data("CoolApp/files/survey_results.json")

    surveyManager = SurveysManager()
    surveyManager.insert_all(survey_data["SurveyResults"])
	

    hospital_data = load_data("CoolApp/files/hospitals.json")

    hospitalManager = HospitalsManager()
    hospitalManager.insert_all(hospital_data["hospitals"])


    person_data = load_data("CoolApp/files/persons.json")
	
    personManager = PersonsManager()
    personManager.insert_all(person_data["persons"])


    doctor_data = load_data("CoolApp/files/doctors.json")

    doctorManager = DoctorsManager()
    doctorManager.insert_all(doctor_data["doctors"])


#populate_tables()
