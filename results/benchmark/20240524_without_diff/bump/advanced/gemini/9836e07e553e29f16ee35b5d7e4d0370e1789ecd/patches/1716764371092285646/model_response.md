```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() throws Exception {
    // Arrange
    final String path = "/docker-adapter/src/test/java/com/artipie/docker/http/UploadEntityRequestTest.java";
    // Act
    final UploadEntityRequest entityRequest = new UploadEntityRequest(path);
    // Assert
    final int status = entityRequest.getStatus();
    assertThat(status).isEqualTo(400);
}
```