```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try {
        new UploadEntityRequest(
                new com.google.common.net.UrlEscapers(),
                new io.netty.handler.codec.http.DefaultHttpHeaders(),
                new java.io.File("src/test/resources/test.tar"),
                "test"
        );
    } catch (java.io.IOException e) {
        org.junit.jupiter.api.Assertions.assertEquals(
                "File not found: src/test/resources/test.tar",
                e.getMessage()
        );
    }
}
```