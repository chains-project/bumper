```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try (HttpClient client = HttpClientBuilder.create().build()) {
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("http://localhost:8080/v2/"))
                .headers(Headers.of("Authorization", "Basic " + Base64.getEncoder().encodeToString("admin:admin".getBytes(StandardCharsets.UTF_8))))
                .post(HttpRequest.BodyPublishers.ofString("{\"image\":\"test\",\"fromImage\":\"test\",\"tag\":\"latest\"}"))
                .build();
        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        assertEquals(400, response.statusCode());
        assertThat(response.body()).contains("Invalid path");
    } catch (IOException e) {
        fail(e);
    }
}
```