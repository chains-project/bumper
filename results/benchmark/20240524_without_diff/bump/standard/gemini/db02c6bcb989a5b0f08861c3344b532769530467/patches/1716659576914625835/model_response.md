```java
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    var request = new UploadEntityRequest(new byte[0], "invalid", "sha256:1234567890");
    var exception = assertThrows(IllegalArgumentException.class, () -> request.getUploadPath());
    assertEquals("Invalid path: invalid", exception.getMessage());
}
```