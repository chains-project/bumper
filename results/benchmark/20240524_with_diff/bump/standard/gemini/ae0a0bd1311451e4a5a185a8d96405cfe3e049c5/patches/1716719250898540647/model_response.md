```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
  final String path = "/docker-adapter/src/test/java/com/artipie/docker/http/UploadEntityRequestTest.java";
  final int line = 87;
  final int column = 281;
  final String expected = ";";
  try {
    new UploadEntityRequest(new ByteArrayInputStream(new byte[0]), path, line, column, expected);
    fail("Should throw exception on invalid path");
  } catch (final IllegalArgumentException e) {
    // Expected
  }
}
```