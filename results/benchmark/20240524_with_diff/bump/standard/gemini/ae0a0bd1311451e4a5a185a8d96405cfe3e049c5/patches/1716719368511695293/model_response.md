```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // The test should throw an exception when the path is invalid.
    assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntityRequest(
            new ByteArrayInputStream(new byte[0]),
            new String[]{},
            "invalid-path",
            null
        )
    );
}
```