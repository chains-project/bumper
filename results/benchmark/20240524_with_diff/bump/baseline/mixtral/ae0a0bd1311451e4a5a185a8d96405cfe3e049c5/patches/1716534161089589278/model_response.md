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
            new StringStartsWith("Unexpected query")
        );
    }
```
In this patch, I replaced the `StringContains` matcher with `StringStartsWith`, which only requires a single argument. This should resolve the compilation error caused by the changes in the library version.