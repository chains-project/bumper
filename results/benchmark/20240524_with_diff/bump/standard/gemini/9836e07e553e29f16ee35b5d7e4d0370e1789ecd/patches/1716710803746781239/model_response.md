```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // TODO: review this AI generated patch!
    try {
        // TODO: review this AI generated patch!
        new java.io.FileOutputStream("invalid_path");
    } catch (java.io.IOException e) {
        // TODO: review this AI generated patch!
        org.junit.jupiter.api.Assertions.assertEquals(
            "java.io.FileNotFoundException: invalid_path (No such file or directory)",
            e.getMessage()
        );
    }
}
```