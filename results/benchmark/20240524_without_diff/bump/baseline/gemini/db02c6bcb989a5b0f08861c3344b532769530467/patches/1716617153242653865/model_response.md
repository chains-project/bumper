```java
  @Test
    public void shouldThrowExceptionWhenDigestIsAbsent() {
        RequestLine requestLine = new RequestLine(RqMethod.PUT, "/v2/my-repo/blobs/uploads/123-abc?what=nothing");
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> new UploadEntity.Request(requestLine.toString()).digest(),
                new StringContains(false, "Unexpected query")
            );
    }
```