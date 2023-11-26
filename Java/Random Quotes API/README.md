# Random Quotes API

This API fetches data from /src/main/resources/quotes.json when a request is made from a server.This json contains a limited list of quotes for now which can be extended according to your use.

# How to Run

## Build After Skipping Tests
```
./mvnw clean install -DskipTests
```

## Run the Build
```
java -jar target/quotes-0.0.1-SNAPSHOT.jar
```

## Make Requests

```
http://localhost:8080/api/quotes
```