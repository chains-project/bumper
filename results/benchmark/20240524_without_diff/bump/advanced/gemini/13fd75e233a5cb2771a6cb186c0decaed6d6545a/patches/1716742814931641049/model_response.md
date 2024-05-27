```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "/invalid-path";

    // Act
    final RuntimeException exception = org.junit.jupiter.api.Assertions.assertThrows(RuntimeException.class, () -> {
        new com.artipie.docker.http.UploadEntityRequest(path);
    });

    // Assert
    org.junit.jupiter.api.Assertions.assertEquals("Invalid path: " + path, exception.getMessage());
}
```