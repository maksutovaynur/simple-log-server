# simple-log-server
Simple server for client's logging

## Main Commands
#### Run

    ./manage.sh run
    
Data for MongoDB will be stored in `.data` folder.


#### Stop

    ./manage.sh stop
    
#### Generate new user token

    ./manage.sh token-add
    
## API
Example with curl:
    
    curl --header "Content-Type: application/json"   --request POST   --data '{"user_token":"9e176ee12b7a47c8a2d4033871deb551", "log_data": {"text": "ok"}}' http://localhost:8080/logs
    
You also can see swagger ui in `http://localhost:8080/docs`
    
## Customization
You can change variables, using `.env` file in project root. See examples in `example.env` file.
