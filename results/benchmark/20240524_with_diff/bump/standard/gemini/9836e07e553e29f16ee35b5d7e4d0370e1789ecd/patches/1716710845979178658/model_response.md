```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    Assert.assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntityRequest("invalid path")
    );
}
```