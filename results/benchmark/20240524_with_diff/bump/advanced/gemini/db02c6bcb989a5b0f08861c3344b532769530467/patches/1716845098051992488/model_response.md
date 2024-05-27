```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() throws Exception {
    final var request = new com.artipie.docker.http.UploadEntityRequest(
        new java.io.ByteArrayInputStream(new byte[0]), 10,
        new com.artipie.docker.http.UploadEntityRequest.Headers() {
            @Override
            public java.util.Map<String, String> headers() {
                return java.util.Collections.emptyMap();
            }
        }
    );
    org.junit.jupiter.api.Assertions.assertThrows(
        com.artipie.docker.http.UploadEntityRequest.InvalidPathException.class,
        () -> request.path()
    );
}
```