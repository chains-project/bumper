```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String invalidPath = "invalid/path";
    final String message = "Invalid path: " + invalidPath;

    // Act
    final UploadEntityRequest request = new UploadEntityRequest(invalidPath);

    // Assert
    final Exception exception = Assertions.assertThrows(Exception.class, request::execute);
    Assertions.assertEquals(message, exception.getMessage());
}
```