```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalid/path";
    final String payload = "payload";
    final byte[] data = payload.getBytes(StandardCharsets.UTF_8);
    final InputStream stream = new ByteArrayInputStream(data);
    final UploadEntityRequest request = new UploadEntityRequest(path, stream, data.length, new HashMap<>());

    // Act & Assert
    assertThrows(
            IllegalArgumentException.class,
            () -> request.validate()
    );
}
```