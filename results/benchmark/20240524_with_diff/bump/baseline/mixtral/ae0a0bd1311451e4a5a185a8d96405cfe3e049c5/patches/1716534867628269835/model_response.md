Here's the fixed `shouldThrowExceptionWhenDigestIsAbsent` method:

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
        new StringStartsWith("Unexpected query") // Changed to use StringStartsWith instead of StringContains
    );
}
```

The issue was caused by the incorrect usage of the `StringContains` matcher. It expects a single argument, the expected substring. However, it was called with two arguments, a boolean and a string. I replaced it with the `StringStartsWith` matcher, which checks if the actual string starts with the given substring. This should resolve the error and make the test pass.