```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final String path = "invalid";
    final HttpURLConnection connection = new HttpURLConnection(new URL(path)) {
        @Override
        public void connect() throws IOException {
            throw new IOException("Test exception");
        }
    };
    final UploadEntityRequest request = new UploadEntityRequest(new InputStream() {
        @Override
        public int read() throws IOException {
            return 0;
        }
    }, connection);

    // Act
    final CompletableFuture<Void> result = request.execute();

    // Assert
    assertThatThrownBy(result::get)
            .hasMessage("Test exception")
            .isInstanceOf(IOException.class);
}
```