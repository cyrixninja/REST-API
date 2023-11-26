# Dictionary API

Dataset used for making this API - [Dataset](https://github.com/matthewreagan/WebstersEnglishDictionary) 

This API fetches data from /src/main/resources/dictionary.json when a request is made from a server.

# How to Run

## Build After Skipping Tests
```
./mvnw clean install -DskipTests
```

## Run the Build
```
  java -jar target/dictionary-0.0.1-SNAPSHOT.jar
```

## Make Requests

```
http://localhost:8080/api/dictionary/{word}
```