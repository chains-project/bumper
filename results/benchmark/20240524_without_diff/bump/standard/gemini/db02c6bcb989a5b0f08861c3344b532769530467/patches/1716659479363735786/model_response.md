```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  // Arrange
  final String path = "/path/to/file";
  final String content = "content";
  final String contentType = "application/octet-stream";
  final long length = content.length();
  final String url = "http://localhost:8080";
  final String token = "Bearer token";
  final UploadEntityRequest request = new UploadEntityRequest(path, content, contentType, length, url, token);
  // Act
  final Entity entity = request.getEntity();
  // Assert
  assertThat(entity).isNotNull();
}
```