```java
  @Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> {
                    RequestLine requestLine = new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    );
                    return new UploadEntity.Request(requestLine.toString()).digest();
                },
                new StringContains(false, "Unexpected query")
            );
    }
```