```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    assertThrows(
        IOException.class,
        () -> new UploadEntityRequest(
            new java.net.URI("http://localhost:8080/docker/v1/images/create"),
            new java.io.File("/tmp/test.tar"),
            "test",
            new java.util.HashMap<>()
        )
    );
}
```