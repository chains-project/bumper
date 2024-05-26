```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalid/path";
    final String message = "Invalid path: " + path;

    // Act & Assert
    assertThrows(
        IllegalArgumentException.class,
        message,
        () -> new UploadEntityRequest(path)
    );
}
```