```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final var actual = new com.artipie.docker.http.UploadEntityRequest(com.artipie.asto.Content.EMPTY, "invalid path");
    org.junit.jupiter.api.Assertions.assertThrows(java.io.IOException.class, () -> actual.send(null, null, null));
}
```