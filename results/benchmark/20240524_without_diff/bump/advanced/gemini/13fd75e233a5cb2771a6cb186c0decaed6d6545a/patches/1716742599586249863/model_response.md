```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final var url = new URL("http://example.com/path");
    final var connection = url.openConnection();
    final var request = new UploadEntityRequest(connection);
    final var response = request.send(new byte[0]);
    org.junit.jupiter.api.Assertions.assertThrows(IOException.class, response::readEntity);
}
```