```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    final String requestLine = new RequestLine(
        RqMethod.PUT,
        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
    ).toString();
  
    final IllegalStateException exception = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(requestLine).digest()
    );

    MatcherAssert.assertThat(
        exception.getMessage(),
        Matchers.containsString("Unexpected query")
    );
}
```