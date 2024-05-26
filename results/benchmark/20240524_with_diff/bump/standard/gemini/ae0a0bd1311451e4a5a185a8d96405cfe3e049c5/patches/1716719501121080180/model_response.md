```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    assertThatThrownBy(() -> new UploadEntityRequest(new HttpConnection.Response(400, "Bad Request", Map.of(), new ByteArrayInputStream(new byte[0])), "foo", "bar"))
            .isInstanceOf(UploadEntityRequest.InvalidPathException.class);
}
```