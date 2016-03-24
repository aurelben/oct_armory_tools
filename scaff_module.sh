echo "Create the module directory inside the *app* module"
mkdir ./project/$1

echo "Create where module's templates will reside"
mkdir ./project/$1/templates/

echo "Create __init__.py to set the directory as a Python module"
touch ./project/$1/__init__.py

echo "Create module's controllers and models etc."
touch ./project/$1/controllers.py
touch ./project/$1/models.py
touch ./project/$1/forms.py

echo  "Create module's templates"
touch ./project/$1/templates/signin.html
