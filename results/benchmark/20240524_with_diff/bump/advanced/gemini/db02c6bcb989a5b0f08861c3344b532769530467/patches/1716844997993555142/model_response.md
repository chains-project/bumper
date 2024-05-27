```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final var request = new org.eclipse.jetty.client.api.Request();
    request.path("/invalid/path");

    // Act & Assert
    org.junit.jupiter.api.Assertions.assertThrows(org.eclipse.jetty.client.api.Request.InvalidRequestException.class, () -> request.path("/invalid/path"));
}
```