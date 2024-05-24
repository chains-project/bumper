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

The change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which only takes a single string argument. This is because the library version you're using has removed the `StringContains` constructor that takes a boolean argument, which is causing the compilation error. The `StringStartsWith` matcher checks if the input string starts with the given substring, which should be sufficient for your test case.