```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // TODO: review this AI generated patch!
    HttpRequest.HttpRequestBuilder builder = HttpRequest.newBuilder();
    builder.GET();
    builder.uri(URI.create("http://localhost:8080/v1/repositories/test/tags/test"));
    builder.header("Authorization", "Basic " + Base64.getEncoder().encodeToString("user:password".getBytes()));
    HttpRequest request = builder.build();
    HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
    assertEquals(404, response.statusCode());
}
```