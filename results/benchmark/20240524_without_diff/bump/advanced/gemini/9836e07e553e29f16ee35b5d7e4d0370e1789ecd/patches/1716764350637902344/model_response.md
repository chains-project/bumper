```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalid/path";
    final String entity = "entity";

    // Act & Assert
    assertThrows(
        DockerException.class,
        () -> new UploadEntityRequest(
            new UploadEntityRequest.Target(path),
            new ByteArrayInputStream(entity.getBytes())
        )
    );
}
```