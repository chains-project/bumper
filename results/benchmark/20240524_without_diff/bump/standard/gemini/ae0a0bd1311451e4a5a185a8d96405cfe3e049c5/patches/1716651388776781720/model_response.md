```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String invalidPath = "invalid/path";
    final String expectedMessage = "Invalid path: " + invalidPath;

    // Act
    final Exception exception = org.junit.jupiter.api.Assertions.assertThrows(
        com.artipie.http.ResponseException.class,
        () -> new com.artipie.docker.http.UploadEntityRequest(
            new com.artipie.http.SimpleResponse(
                java.net.HttpURLConnection.HTTP_BAD_REQUEST,
                "Invalid path",
                new java.io.ByteArrayInputStream(invalidPath.getBytes())
            )
        ).entity()
    );

    // Assert
    org.junit.jupiter.api.Assertions.assertEquals(expectedMessage, exception.getMessage());
}
```