# Literate Parakeet
This is the admin side of the Mogen project

## API Doc
The endpoints are available at requests.http file

## How to contribute
* Fork and download the repository
* Copy the file **env-sample**, rename to **.env** and put your env variables
* Run
    * `docker compose up`
    * `docker exec <container_id> python manage.py db migrate`

* Code and then open a PR ;)