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

The change made here is to replace `new StringContains(false, "Unexpected query")` with `new StringStartsWith("Unexpected query")`. This is because the constructor for `StringContains` has changed in the new library version and no longer accepts a boolean parameter. Instead, you can use `StringStartsWith` to check if the message starts with the specified string.