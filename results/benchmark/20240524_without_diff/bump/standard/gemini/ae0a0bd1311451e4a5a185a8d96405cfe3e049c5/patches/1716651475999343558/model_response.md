```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try {
        new UploadEntityRequest(
                new org.apache.http.client.methods.HttpGet("/does-not-exist"),
                org.apache.http.entity.ContentType.APPLICATION_OCTET_STREAM
        );
        org.junit.jupiter.api.Assertions.fail("Should have thrown exception");
    } catch (final java.io.IOException e) {
        // expected
    }
}
```