```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "/invalid/path";

    // Act & Assert
    assertThrows(RuntimeException.class, () -> new UploadEntityRequest(path));
}
```