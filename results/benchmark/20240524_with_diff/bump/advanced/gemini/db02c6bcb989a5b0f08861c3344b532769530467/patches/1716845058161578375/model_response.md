```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  // Arrange
  final String path = "/some/invalid/path";
  final byte[] body = new byte[0];

  // Act
  final UploadEntityRequest request = new UploadEntityRequest(path, body);

  // Assert
  assertThrows(IllegalArgumentException.class, request::execute);
}
```