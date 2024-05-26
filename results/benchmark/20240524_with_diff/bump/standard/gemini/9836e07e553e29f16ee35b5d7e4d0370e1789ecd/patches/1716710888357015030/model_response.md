```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    String path = "invalid path";
    assertThrows(RuntimeException.class, () -> new UploadEntityRequest(path));
}
```