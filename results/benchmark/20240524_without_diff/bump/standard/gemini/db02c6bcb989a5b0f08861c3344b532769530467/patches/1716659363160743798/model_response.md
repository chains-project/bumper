```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalid/path";
    final String content = "content";
    final String token = "token";
    final String url = "url";
    final String message = "message";
    final String expectedMessage = "Invalid path: invalid/path";

    // Act & Assert
    final Exception exception = org.junit.jupiter.api.Assertions.assertThrows(
        org.eclipse.jetty.client.HttpResponseException.class,
        () -> new com.artipie.docker.http.UploadEntityRequest(
            path,
            content,
            token,
            url,
            message
        )
    );
    org.junit.jupiter.api.Assertions.assertEquals(expectedMessage, exception.getMessage());
}
```