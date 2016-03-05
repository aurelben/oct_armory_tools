echo "Create the module directory inside the *app* module"
mkdir ./app/$1

echo "Create where module's templates will reside"
mkdir ./app/templates/$1

echo "Create __init__.py to set the directory as a Python module"
touch ./app/$1/__init__.py

echo "Create module's controllers and models etc."
touch ./app/$1/controllers.py
touch ./app/$1/models.py
touch ./app/$1/forms.py

echo  "Create module's templates"
touch ./app/templates/$1/signin.html
