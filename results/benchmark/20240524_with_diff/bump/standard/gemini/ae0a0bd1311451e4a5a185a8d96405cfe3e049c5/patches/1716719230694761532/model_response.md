```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    String invalidPath = "invalid/path";

    // Act & Assert
    assertThrows(IllegalArgumentException.class, () -> new UploadEntityRequest(invalidPath));
}
```