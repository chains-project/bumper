```java
  // TODO: review this AI generated patch!
  @Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> {
                    RequestLine requestLine = new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc"
                    );
                    return new UploadEntity.Request(requestLine.toString()).digest();
                }),
                Matchers.containsString("Unexpected query")
            );
    }
```