Here's a possible patch for the failing code:

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
        new StringStartsWith("Unexpected query") // use StringStartsWith instead of StringContains
    );
}
```

The failure is caused by the `StringContains` constructor, which now requires a single `String` argument instead of a `boolean` and a `String`. To fix the error, I replaced `StringContains` with `StringStartsWith`, which has a similar behavior and accepts a single `String` argument.