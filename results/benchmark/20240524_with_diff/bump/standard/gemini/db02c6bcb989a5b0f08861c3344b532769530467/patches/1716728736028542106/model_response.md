```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "/invalid/path";
    final String expectedMessage = "Invalid path: " + path;

    // Act
    final Exception exception = org.junit.jupiter.api.Assertions.assertThrows(
        org.apache.http.client.HttpResponseException.class,
        () -> new UploadEntityRequest(path, null, null, null, null, null, null, null, null)
    );

    // Assert
    org.junit.jupiter.api.Assertions.assertEquals(expectedMessage, exception.getMessage());
}
```