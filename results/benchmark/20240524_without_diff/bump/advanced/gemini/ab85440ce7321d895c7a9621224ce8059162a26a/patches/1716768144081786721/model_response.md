```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    String invalidPath = "/invalid/path";
    String expectedMessage = "Invalid path: " + invalidPath;

    // Act
    UploadEntityRequest entityRequest = new UploadEntityRequest(invalidPath, new ByteArrayInputStream(new byte[0]));
    Exception exception = Assertions.assertThrows(RuntimeException.class, entityRequest::execute);

    // Assert
    Assertions.assertEquals(expectedMessage, exception.getMessage());
}
```