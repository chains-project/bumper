```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    final var uri = new java.net.URI("http://localhost:8080/docker/v1.24/images/create?fromImage=alpine:latest&tag=latest");
    final var http = new org.apache.http.impl.client.HttpClientBuilder().build();
    final var request = new org.apache.http.client.methods.HttpPost(uri);
    final var entity = new org.apache.http.entity.mime.MultipartEntityBuilder().addPart("file", new java.io.File("src/test/resources/alpine.tar")).build();
    request.setEntity(entity);
    try (final var response = http.execute(request)) {
        org.junit.jupiter.api.Assertions.assertEquals(400, response.getStatusLine().getStatusCode());
    } catch (final java.io.IOException e) {
        throw new java.lang.RuntimeException(e);
    }
}
```