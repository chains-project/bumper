```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    assertThrows(
            java.lang.IllegalArgumentException.class,
            () -> new com.artipie.docker.http.UploadEntityRequest(
                    new java.io.File("/invalid/path"),
                    new com.artipie.docker.http.ContentLength(0L)
            )
    );
}
```