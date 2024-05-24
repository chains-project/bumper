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

In the original code, the `StringContains` matcher was instantiated with two arguments, while the constructor only accepts a single argument. The updated library version no longer supports the two-argument constructor. Instead, you can use the `StringStartsWith` matcher to check if the message starts with the expected substring.