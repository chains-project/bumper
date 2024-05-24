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

In the original code, the `StringContains` matcher was used incorrectly. It requires a single argument - the expected substring. However, in the original code, it received two arguments: a boolean value and a string.

I have replaced the `StringContains` matcher with the `StringStartsWith` matcher. This matcher checks if a string starts with a given substring. It only requires a single argument, so it avoids the compilation error.

Note that I have not changed the function signature or removed the `@Override` decorator. Also, I have not used any removed library methods (indicated with `--`). I have only used the `StringStartsWith` matcher, which is a new method added in the updated library (indicated with `++`).