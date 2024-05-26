```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalidPath";
    final String message = "Invalid path";

    // Act & Assert
    assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntityRequest(
            new ByteArrayInputStream(new byte[0]),
            path,
            new HashMap<>(),
            new HashMap<>(),
            new HashMap<>(),
            new HashMap<>(),
            new HashMap<>(),
            new HashMap<>()
        ),
        message
    );
}
```