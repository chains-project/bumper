```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    String path = "/path/to/resource";
    try (CloseableHttpResponse response = new TestHttpClient().execute(new HttpPost(path))) {
        assertEquals(HttpStatus.SC_NOT_FOUND.value(), response.getStatusLine().getStatusCode());
    } catch (IOException e) {
        fail(e);
    }
}
```