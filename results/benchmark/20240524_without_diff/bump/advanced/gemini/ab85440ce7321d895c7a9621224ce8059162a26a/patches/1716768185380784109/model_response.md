```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Create a mock entity request with an invalid path.
    final MockEntityRequest request = new MockEntityRequest(
        "GET",
        "/some/invalid/path"
    );

    // Assert that an exception is thrown when the request is executed.
    assertThrows(
        IllegalArgumentException.class,
        () -> request.execute()
    );
}
```