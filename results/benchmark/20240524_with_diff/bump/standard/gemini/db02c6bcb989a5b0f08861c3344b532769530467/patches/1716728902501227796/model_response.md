```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalid/path";
    // Act & Assert
    org.junit.jupiter.api.Assertions.assertThrows(
        org.apache.http.client.methods.HttpUriRequest.class,
        () -> new org.apache.http.client.methods.HttpGet(path)
    );
}
```