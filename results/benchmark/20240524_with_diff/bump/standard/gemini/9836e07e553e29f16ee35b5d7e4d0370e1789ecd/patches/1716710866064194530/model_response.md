```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  // Arrange
  String invalidPath = "/";

  // Act & Assert
  assertThrows(RuntimeException.class, () -> new UploadEntityRequest(new DummyClient(), invalidPath));
}
```