Here's the proposed patch:

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

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher. The `StringContains` matcher has been changed in the new library version and now requires only one argument, while the code still passes two arguments. The `StringStartsWith` matcher has the same behavior as the old `StringContains` matcher, and it only requires one argument, so it can be used as a drop-in replacement.