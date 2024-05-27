```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() throws Exception {
    // given
    String body = "invalid body";
    // when
    try {
        new UploadEntityRequest(new ByteArrayInputStream(body.getBytes("UTF-8")), "invalid path");
        fail("Should throw exception on invalid path");
    } catch (IllegalArgumentException e) {
        // then
        assertThat(e.getMessage()).isEqualTo("Invalid path: invalid path");
    }
}
```