```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final String path = "/docker-adapter/src/test/java/com/artipie/docker/http/UploadEntityRequestTest.java";
    final int line = 87;
    final int column = 343;
    final String message = "';' expected";
    final Exception exception = new Exception(message);
    try {
        new UploadEntityRequestTest().shouldThrowExceptionOnInvalidPath();
        fail("Should have thrown an exception");
    } catch (final Exception e) {
        assertEquals(message, e.getMessage());
        assertEquals(path, e.getStackTrace()[0].getFileName());
        assertEquals(line, e.getStackTrace()[0].getLineNumber());
        assertEquals(column, e.getStackTrace()[0].getColumnNumber());
        assertSame(exception, e.getCause());
    }
}
```