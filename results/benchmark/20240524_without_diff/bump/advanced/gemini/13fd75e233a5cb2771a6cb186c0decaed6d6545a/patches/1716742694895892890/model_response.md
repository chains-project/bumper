```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final var request = new org.apache.http.client.methods.HttpEntityEnclosingRequestBase() {
        @Override
        public String getMethod() {
            return "POST";
        }
    };
    request.setURI(new java.net.URI("http://localhost:8081/v1/repositories/test-repo/images/test-image/tags/test-tag"));
    final var entity = org.mockito.Mockito.mock(org.apache.http.HttpEntity.class);
    request.setEntity(entity);

    // Act
    org.junit.jupiter.api.Assertions.assertThrows(org.apache.http.client.HttpResponseException.class, () -> {
        new com.artipie.docker.http.UploadEntityRequest(request).send(new org.apache.http.impl.client.CloseableHttpClient());
    });
}
```