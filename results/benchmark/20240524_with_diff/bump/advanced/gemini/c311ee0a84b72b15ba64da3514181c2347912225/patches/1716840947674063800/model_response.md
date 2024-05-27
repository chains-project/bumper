```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try {
        new com.artipie.docker.http.UploadEntityRequest(
                new com.artipie.http.Headers.From(new com.artipie.http.Pair<>("Content-Type", "application/json")),
                new java.io.ByteArrayInputStream("{\"path\":\"/invalid/path\"}".getBytes(java.nio.charset.StandardCharsets.UTF_8))
        );
        org.junit.jupiter.api.Assertions.fail("Should throw exception on invalid path");
    } catch (com.artipie.docker.http.UploadEntityRequest.InvalidPathException e) {
        // Expected
    }
}
```