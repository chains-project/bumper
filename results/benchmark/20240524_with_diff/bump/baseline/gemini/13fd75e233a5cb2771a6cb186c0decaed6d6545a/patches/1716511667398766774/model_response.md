```java
  // TODO: review this AI generated patch!
 @Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        String requestLine = new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
        ).toString();
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> new UploadEntity.Request(requestLine).digest(),
                new StringContains(false, "Unexpected query")
            );
    }
```