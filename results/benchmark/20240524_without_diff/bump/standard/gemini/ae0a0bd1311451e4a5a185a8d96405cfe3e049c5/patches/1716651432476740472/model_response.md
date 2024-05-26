```java
// TODO: review this AI generated patch!
@org.junit.jupiter.api.Test
void shouldThrowExceptionOnInvalidPath() throws org.apache.http.client.HttpResponseException {
  // TODO: review this AI generated patch!
  org.apache.http.HttpResponse response = org.mockito.Mockito.mock(org.apache.http.HttpResponse.class);
  org.mockito.Mockito.when(response.getStatusLine()).thenReturn(new org.apache.http.StatusLine() {
    @Override
    public int getStatusCode() {
      return 404;
    }

    @Override
    public org.apache.http.ProtocolVersion getProtocolVersion() {
      return org.apache.http.HttpVersion.HTTP_1_1;
    }

    @Override
    public java.lang.String getReasonPhrase() {
      return "Not Found";
    }
  });
  org.apache.http.HttpEntity entity = org.mockito.Mockito.mock(org.apache.http.HttpEntity.class);
  org.mockito.Mockito.when(response.getEntity()).thenReturn(entity);
  org.mockito.Mockito.when(entity.getContent()).thenReturn(new java.io.ByteArrayInputStream("Not Found".getBytes()));
  org.mockito.Mockito.when(entity.getContentType()).thenReturn(new org.apache.http.entity.ContentType("text/plain"));
  org.mockito.Mockito.doThrow(new org.apache.http.client.HttpResponseException(response)).when(this.client).execute(org.mockito.Mockito.any(org.apache.http.client.methods.HttpRequestBase.class));
  org.junit.jupiter.api.Assertions.assertThrows(com.artipie.http.ResponseException.class, () -> {
    this.upload.upload(new java.io.File("src/test/resources/com/artipie/docker/http/upload/simple.tar"), new java.io.ByteArrayInputStream("simple".getBytes()));
  });
}
```