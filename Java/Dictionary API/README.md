# SpringBoot REST API Example 3 (Dictionary API)

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