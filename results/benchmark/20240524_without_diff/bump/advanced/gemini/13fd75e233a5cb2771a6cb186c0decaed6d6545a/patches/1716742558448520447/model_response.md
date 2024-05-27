```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    String path = "invalid";

    // Act
    try {
        new UploadEntityRequest(path);
        org.junit.jupiter.api.Assertions.fail("Should have thrown an exception");
    } catch (IllegalArgumentException e) {
        // Assert
        org.junit.jupiter.api.Assertions.assertEquals("Invalid path: " + path, e.getMessage());
    }
}
```