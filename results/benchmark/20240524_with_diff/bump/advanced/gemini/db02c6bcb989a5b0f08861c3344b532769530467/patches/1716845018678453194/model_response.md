```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() {
    // Arrange
    final var request = new org.apache.http.client.methods.HttpPost("http://localhost:8080/v1/images/create?fromImage=busybox&tag=latest");
    request.setEntity(new org.apache.http.entity.StringEntity("{\"image\":\"busybox\",\"tag\":\"latest\",\"fromImage\":\"busybox\",\"message\":\"test\",\"author\":\"test\"}", org.apache.http.entity.ContentType.APPLICATION_JSON));
    final var response = new org.apache.http.HttpResponse() {
        @Override
        public int getStatusCode() {
            return 400;
        }

        @Override
        public org.apache.http.HttpEntity getEntity() {
            return new org.apache.http.entity.StringEntity("{\"message\":\"Image is not found\",\"code\":\"image_not_found\"}", org.apache.http.entity.ContentType.APPLICATION_JSON);
        }

        @Override
        public org.apache.http.Header[] getHeaders(String name) {
            return new org.apache.http.Header[0];
        }

        @Override
        public org.apache.http.Header[] getAllHeaders() {
            return new org.apache.http.Header[0];
        }
    };
    // Act
    final var exception = org.junit.jupiter.api.Assertions.assertThrows(
            com.artipie.docker.http.UploadEntityRequest.UploadException.class,
            () -> new com.artipie.docker.http.UploadEntityRequest(request, response)
    );
    // Assert
    org.junit.jupiter.api.Assertions.assertEquals("Image is not found", exception.getMessage());
}
```