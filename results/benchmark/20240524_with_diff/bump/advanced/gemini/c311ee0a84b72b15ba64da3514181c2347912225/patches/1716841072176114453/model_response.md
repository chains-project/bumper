```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final var exception = org.junit.jupiter.api.Assertions.assertThrows(
        com.artipie.asto.net.UncheckedIOException.class,
        () -> new com.artipie.docker.http.UploadEntityRequest(
            new com.artipie.http.async.AsyncResponse(),
            "path",
            com.artipie.asto.Content.EMPTY
        )
    );
    org.junit.jupiter.api.Assertions.assertEquals("Invalid path: path", exception.getMessage());
}
```