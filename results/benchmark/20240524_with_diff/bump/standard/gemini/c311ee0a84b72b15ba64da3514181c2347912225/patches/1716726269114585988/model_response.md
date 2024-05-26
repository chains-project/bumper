```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final String path = "/invalid/path";
    final String message = "Invalid path: " + path;
    final RuntimeException exception = new RuntimeException(message);
    assertThrows(exception.getClass(), () -> new UploadEntityRequest(path));
}
```