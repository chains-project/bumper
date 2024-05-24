Here's the fixed version of the code:

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

The change is to replace `new StringContains(false, "Unexpected query")` with `new StringStartsWith("Unexpected query")`. The `StringContains` constructor that takes a boolean and a string has been removed in the new library version, and the error message indicates that the boolean argument is not expected. Instead, we can use the `StringStartsWith` matcher to check if the message starts with the expected substring.