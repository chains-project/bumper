Here is the proposed patch:
```java
    @Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString()
                )
            ).getMessage(),
            new StringStartsWith("Unexpected query")
        );
    }
```
The change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which has the expected signature. This should fix the error.