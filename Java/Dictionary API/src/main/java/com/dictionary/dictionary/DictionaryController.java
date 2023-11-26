package com.dictionary.dictionary;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.io.InputStream;
import java.util.Map;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

@RestController
@RequestMapping("/api/dictionary")
public class DictionaryController {
    private final Map<String, String> dictionary;

    public DictionaryController() throws IOException {
        ObjectMapper mapper = new ObjectMapper();
        InputStream inputStream = getClass().getResourceAsStream("/dictionary.json");
        this.dictionary = mapper.readValue(inputStream, new TypeReference<Map<String, String>>() {});
    }

    @GetMapping("/{word}")
    public String getMeaning(@PathVariable String word) {
        return dictionary.getOrDefault(word, "Meaning not found for the word: " + word);
    }
}
