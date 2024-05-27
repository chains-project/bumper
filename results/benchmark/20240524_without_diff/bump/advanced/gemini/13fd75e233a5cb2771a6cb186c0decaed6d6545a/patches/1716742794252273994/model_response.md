```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String invalidPath = "invalid/path";

    // Act & Assert
    assertThrows(
        IllegalArgumentException.class,
        () -> new UploadEntityRequest(
            new DummyResponse(),
            new DummyResponse(),
            new DummyResponse(),
            invalidPath,
            Optional.empty()
        )
    );
}
```