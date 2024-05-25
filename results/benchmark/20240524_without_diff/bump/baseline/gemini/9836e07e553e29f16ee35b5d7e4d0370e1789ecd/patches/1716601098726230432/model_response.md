```java
@Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> {
                    String url = new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString();
                    return new UploadEntity.Request(url).digest();
                },
                new StringContains(false, "Digest is required")
            );
    }
```