```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    try {
        new UploadEntityRequest(new java.net.URI("http://localhost:8080/docker-api/images/create?fromImage=alpine:latest&tag=test&fromSrc=/tmp/test.tar"), new java.io.ByteArrayInputStream(new byte[0]), 1000);
        org.junit.jupiter.api.Assertions.fail("Should fail with IllegalArgumentException");
    } catch (java.lang.IllegalArgumentException e) {
        // expected
    }
}
```