```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final String path = "invalid-path";
    final String message = "Invalid path: " + path;
    assertThrows(IllegalArgumentException.class, () -> new UploadEntityRequest(path), message);
}
```