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

The change made is to replace `new StringContains(false, "Unexpected query")` with `new StringStartsWith("Unexpected query")`. It seems like the `StringContains` constructor that takes a boolean argument has been removed in the new library version, so we need to use a different matcher to check if the message starts with the expected string.