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
        new StringStartsWith("Unexpected query") // modified
    );
}
```

The change is to replace `new StringContains(false, "Unexpected query")` with `new StringStartsWith("Unexpected query")`. It seems that the `StringContains` constructor that accepts a boolean argument has been removed in the updated library version. Instead, you can use the `StringStartsWith` matcher to check if the message starts with the expected substring.