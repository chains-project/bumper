```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String invalidPath = "invalid/path";
    final String expectedMessage = "Invalid path: " + invalidPath;

    // Act
    final Exception exception = org.junit.jupiter.api.Assertions.assertThrows(
        java.lang.IllegalArgumentException.class,
        () -> new com.artipie.docker.http.UploadEntityRequest(new java.net.URI(invalidPath))
    );

    // Assert
    org.junit.jupiter.api.Assertions.assertEquals(expectedMessage, exception.getMessage());
}
```