```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    assertThrows(RuntimeException.class, () -> new UploadEntityRequest(new ByteArrayInputStream(new byte[0]), "invalid/path"));
}
```