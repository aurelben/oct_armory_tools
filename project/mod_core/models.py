from peewee import *
import datetime

psql_db = PostgresqlDatabase('aurel', user='aurel')

class BaseModel(Model):
    """A base model that will use our Postgresql database"""
    class Meta:
        database = psql_db

class Officer(BaseModel):
    name = CharField(null = True)
    create_date = DateTimeField(default=datetime.datetime.now)
    email = CharField(null = True)
    password = CharField(null = True)
    github_id = CharField(null = True)
    gh_acces_token = CharField(null = True)


class Plan(BaseModel):
	"""docstring for ClassName"""
	owner = ForeignKeyField(Officer, related_name='plans')
	create_date = DateTimeField(default=datetime.datetime.now)
	name = CharField()
	gh_repo_url = CharField(null = True)
	gh_md_url = CharField(null = True)
	armory_info = CharField(null = True)
	gh_zip_url = CharField(null = True)
	gh_tar_url = CharField(null = True)
	last_modif = DateTimeField(default=datetime.datetime.now)


	
		