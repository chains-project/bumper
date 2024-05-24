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

The change is in the `StringContains` matcher, which has been replaced by `StringStartsWith` because the former has been removed in the new library version. The new matcher checks if the actual string starts with the given substring, which is equivalent to the original intent.