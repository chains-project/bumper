```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  // Arrange
  // Act
  // Assert
  org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalArgumentException.class, () -> {
    new com.artipie.docker.http.UploadEntityRequest(
      new org.eclipse.jetty.server.Request(
        "GET",
        "/docker/images/create?fromImage=invalidPath",
        "HTTP/1.1",
        new java.util.HashMap<>(),
        new java.io.ByteArrayInputStream(new byte[0])
      ),
      "invalidPath"
    );
  });
}
```