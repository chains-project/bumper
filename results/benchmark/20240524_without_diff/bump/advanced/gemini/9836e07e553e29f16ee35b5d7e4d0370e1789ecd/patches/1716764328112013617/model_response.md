```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Given
    String path = "/invalid/path";

    // When
    assertThrows(RuntimeException.class, () -> new UploadEntityRequest(path, null));

    // Then
    // Assertions are done in the Exception assertion
}
```