from peewee import *
from playhouse.migrate import *
import datetime

my_db = PostgresqlDatabase('aurel', user='aurel')
migrator = PostgresqlMigrator(my_db)

# name = CharField(null = True)
# create_date = DateTimeField(default=datetime.datetime.now)
# email = CharField(null = True)
# password = CharField(null = True)
# github_id = CharField(null = True)
# gh_acces_token = CharField(null = True)

migrate(
	migrator.drop_not_null('officer', 'name'),
	migrator.drop_not_null('officer', 'email'),
	migrator.drop_not_null('officer', 'password'),
	migrator.drop_not_null('officer', 'github_id'),
	migrator.drop_not_null('officer', 'gh_acces_token'),

	# migrator.add_column('officer', 'name', name ),
	# migrator.add_column('officer', 'create_date', create_date),
	# migrator.add_column('officer', 'email', email ),
	# migrator.add_column('officer', 'password', password ),
	# migrator.add_column('officer', 'github_id', github_id ),
	# migrator.add_column('officer', 'gh_acces_token', gh_acces_token ),
)

print "donne \n"
