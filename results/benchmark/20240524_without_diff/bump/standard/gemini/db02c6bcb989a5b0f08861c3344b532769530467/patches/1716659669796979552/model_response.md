```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    String invalidPath = "invalidPath";
    org.junit.jupiter.api.Assertions.assertThrows(
        java.nio.file.NoSuchFileException.class,
        () -> new java.io.FileInputStream(invalidPath)
    );
}
```