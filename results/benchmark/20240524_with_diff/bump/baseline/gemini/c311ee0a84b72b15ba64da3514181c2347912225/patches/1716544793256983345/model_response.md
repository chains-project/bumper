```java
  // TODO: review this AI generated patch!
  @Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> {
                    String requestLine = new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString();
                    UploadEntity.Request request = new UploadEntity.Request(requestLine);
                    request.digest();
                },
                Matchers.containsString("Unexpected query")
            );
    }
```