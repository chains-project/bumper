```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try (final var client = new com.artipie.http.client.jetty.JettyClient()) {
        client.put(new java.net.URI("http://localhost:8080/v2/repositories/test/"),
                new com.artipie.http.headers.Header("Content-Type", "application/json"),
                new com.artipie.http.headers.Header("Authorization", "Basic dGVzdDp0ZXN0"),
                new com.artipie.http.rs.StandardRs(new java.io.ByteArrayInputStream("{\"name\":\"test\"}".getBytes())));
    } catch (final java.io.IOException e) {
        org.junit.jupiter.api.Assertions.assertEquals(400, ((com.artipie.http.Response) e).code());
    }
}
```