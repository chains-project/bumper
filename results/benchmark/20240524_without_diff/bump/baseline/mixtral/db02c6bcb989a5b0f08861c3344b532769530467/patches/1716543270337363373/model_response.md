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

The change I made was to replace the `StringContains` matcher with the `StringStartsWith` matcher. The `StringContains` constructor that takes a boolean argument has been removed in the new library version, hence the error message. The `StringStartsWith` matcher, on the other hand, satisfies the requirement of checking if the message starts with the expected substring.