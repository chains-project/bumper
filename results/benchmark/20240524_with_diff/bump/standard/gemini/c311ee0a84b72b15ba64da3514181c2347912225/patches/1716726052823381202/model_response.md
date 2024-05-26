```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final var path = "invalid";
    final var url = "http://localhost:8080/docker/v1/images/create?fromImage=alpine:latest&tag=test";
    final var request = new org.apache.http.client.methods.HttpPost(url);
    final var entity = new com.artipie.docker.http.UploadEntityRequest(path, 1024);
    request.setEntity(entity);
    try (final var response = new org.apache.http.impl.client.CloseableHttpClient().execute(request)) {
        org.junit.jupiter.api.Assertions.assertEquals(400, response.getStatusLine().getStatusCode());
    } catch (final java.io.IOException e) {
        org.junit.jupiter.api.Assertions.fail(e);
    }
}
```