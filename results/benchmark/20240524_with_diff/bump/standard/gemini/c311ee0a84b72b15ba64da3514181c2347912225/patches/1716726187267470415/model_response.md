```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String invalidPath = "invalid/path";
    final String expectedMessage = "Invalid path: " + invalidPath;

    // Act
    final Exception exception = org.junit.jupiter.api.Assertions.assertThrows(
        org.eclipse.jetty.client.HttpResponseException.class,
        () -> new com.artipie.docker.http.UploadEntityRequest(
            new org.eclipse.jetty.client.HttpClient(),
            new java.net.URI("http://localhost:8080"),
            invalidPath
        ).send()
    );

    // Assert
    org.junit.jupiter.api.Assertions.assertEquals(expectedMessage, exception.getMessage());
}
```