```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // TODO: review this AI generated patch!
    Assert.assertThrows(
            IllegalArgumentException.class,
            () -> new UploadEntityRequest(
                    new HttpConnection(),
                    new Buffer(),
                    new Random(),
                    new Endpoint.Builder().withPath("invalid-path").build()
            )
    );
}
```