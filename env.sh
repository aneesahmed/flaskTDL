echo "setting  variables"
source env/bin/activate
export SECRET="some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"
export APP_SETTINGS="development"
export DATABASE_URL="postgresql://localhost/flask_api"
