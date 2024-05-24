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
        new StringStartsWith("Unexpected query") // replace contains with startsWith
    );
}
```

The issue was caused by the incorrect usage of the `StringContains` matcher, which accepts only one argument. To fix the issue, replace `StringContains` with `StringStartsWith`, which checks if a string starts with a given substring.