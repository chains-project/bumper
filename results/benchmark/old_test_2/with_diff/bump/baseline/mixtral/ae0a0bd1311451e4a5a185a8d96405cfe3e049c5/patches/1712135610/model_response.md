Here is a possible patch for the failing client code:
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
In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which has the same purpose but a different constructor signature. The `StringContains` matcher in the new library version requires a single string argument, while the `StringStartsWith` matcher requires a string and a prefix. I also changed the `false` argument of `StringContains` to `"Unexpected query"` for `StringStartsWith` to match the error message.

Note that this patch assumes that the error message starts with the string "Unexpected query", as indicated in the original code. If this is not the case, the patch may need to be adjusted accordingly.