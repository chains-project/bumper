```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    Path path = Paths.get("/invalid/path");
    // Act
    // Assert
    assertThrows(IOException.class, () -> new UploadEntityRequest(path));
}
```