Here's a possible patch for the failing client code:
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
            new StringContains("Unexpected query")
        );
    }
```
The only change made is in the `StringContains` constructor. The `false` argument has been removed, as it is not needed and is causing the error. This constructor only requires a single argument, which is the expected substring.