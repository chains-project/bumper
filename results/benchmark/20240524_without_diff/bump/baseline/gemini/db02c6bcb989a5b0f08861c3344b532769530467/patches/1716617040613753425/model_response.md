```java
  // TODO: review this AI generated patch!
@Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString(),
                    null // Add null to the constructor call
                ).digest(),
                new StringContains(false, "Unexpected query")
            );
    }
```