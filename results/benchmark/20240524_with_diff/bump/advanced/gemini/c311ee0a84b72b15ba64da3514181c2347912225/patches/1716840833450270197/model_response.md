```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    String path = "/invalid/path";
    try {
        UploadEntityRequest.create(path);
        fail("Should throw exception on invalid path");
    } catch (IllegalArgumentException e) {
        assertThat(e.getMessage()).isEqualTo("Invalid path: " + path);
    }
}
```