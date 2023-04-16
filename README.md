Installation Steps

-Step1 pull the project

-Step2 run the command docker-compose up

-Step3 run the command docker-compose exec app python manage.py makemigrations

-Step4 run the command docker-compose exec app python manage.py migrate

-Step5 run the following command if dummy users up to 12 should be created for you

      docker-compose exec app python manage.py create_dummy_users

-Step6
  if you would like to test the api in postman then you need a token and this can be created using below command
http POST http://0.0.0.0:8000/api-token-auth/ username='arun@gmail.com' password="arun"


For Postman -- https://api.postman.com/collections/23976429-bb8766c4-3b50-4d07-9153-afb822a0f42f?access_key=PMAT-01GY4THQ7SA07QSY757JEYP5Y5