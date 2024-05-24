Here's the updated code that should fix the error:

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

The only change made is to replace the `StringContains` matcher with `StringStartsWith`. This is because the constructor signature for `StringContains` has changed in the new library version to only accept a single `String` argument. In contrast, `StringStartsWith` still accepts a `String` and a `boolean` argument, so it can be used instead to achieve the same functionality.