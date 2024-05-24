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

In the original code, the `StringContains` matcher was used with two arguments, but the new version of the library only accepts a single argument. To fix this, I replaced `StringContains` with `StringStartsWith`, which only requires a single argument. This matcher checks if the given string starts with the specified substring, which should be sufficient for the test case.