# Random Jokes API

This API fetches data from /src/main/resources/jokes.json when a request is made from a server.This json contains a limited list of jokes for now which can be extended according to your use.

# How to Run

## Build After Skipping Tests
```
./mvnw clean install -DskipTests
```

## Run the Build
```
 java -jar target/jokes-0.0.1-SNAPSHOT.jar
```

## Make Requests

```
http://localhost:8080/api/jokes
```