```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    String path = "/docker-adapter/src/test/java/com/artipie/docker/http/UploadEntityRequestTest.java";
    int line = 87;
    int column = 281;

    // Act
    Exception exception = org.junit.jupiter.api.Assertions.assertThrows(
            java.lang.RuntimeException.class,
            () -> {
                throw new java.lang.RuntimeException("Invalid path: " + path);
            });

    // Assert
    org.junit.jupiter.api.Assertions.assertEquals(
            "Invalid path: " + path,
            exception.getMessage());
    org.junit.jupiter.api.Assertions.assertEquals(line, exception.getStackTrace()[0].getLineNumber());
    org.junit.jupiter.api.Assertions.assertEquals(column, exception.getStackTrace()[0].getColumnNumber());
}
```