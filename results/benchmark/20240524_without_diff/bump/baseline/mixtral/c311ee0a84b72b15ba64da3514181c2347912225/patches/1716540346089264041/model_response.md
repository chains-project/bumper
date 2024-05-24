Here's the fixed version of the failing method:

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
            ).digest()
        ).getMessage(),
        new StringStartsWith("Unexpected query")
    );
}
```

The change made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, as the constructor signature for `StringContains` has changed in the new library version. The `StringStartsWith` matcher checks if the input string starts with the given substring, which should work for the test case.