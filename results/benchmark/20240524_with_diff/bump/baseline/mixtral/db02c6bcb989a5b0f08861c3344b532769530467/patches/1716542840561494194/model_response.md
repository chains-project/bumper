Here's a possible patch that you can apply to the code:

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
        new StringStartsWith("Unexpected query") // changed here
    );
}
```

In the original code, the `StringContains` matcher was used with two arguments, but the new library version only accepts one argument for this constructor. To fix the error, we can replace `StringContains` with `StringStartsWith`, which only requires one argument. This ensures that the code is compatible with the new library version.