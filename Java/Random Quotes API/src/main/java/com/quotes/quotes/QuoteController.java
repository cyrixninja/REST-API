package com.quotes.quotes;

import org.springframework.core.io.ClassPathResource;
import org.springframework.util.StreamUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.Random;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

@RestController
@RequestMapping("/api/quotes")
public class QuoteController {
    private final List<Quote> quotes;

    public QuoteController() throws IOException {
        ObjectMapper mapper = new ObjectMapper();

        // Load quotes from the "quotes.json" file in the resources folder
        ClassPathResource resource = new ClassPathResource("quotes.json");
        try (InputStream inputStream = resource.getInputStream()) {
            String quotesJson = StreamUtils.copyToString(inputStream, StandardCharsets.UTF_8);
            this.quotes = mapper.readValue(quotesJson, new TypeReference<List<Quote>>() {});
        }
    }

    @GetMapping
    public Quote getRandomQuote() {
        Random random = new Random();
        int index = random.nextInt(quotes.size());
        return quotes.get(index);
    }
}
