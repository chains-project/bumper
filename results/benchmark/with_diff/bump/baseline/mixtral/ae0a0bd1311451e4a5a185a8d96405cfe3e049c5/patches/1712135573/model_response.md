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
            ).digest()
        ).getMessage(),
        new StringStartsWith("Unexpected query") // use new 'starts with' matcher instead of 'contains'
    );
}
```

This patch replaces the `StringContains` matcher with a new `StringStartsWith` matcher, which has the same semantics as the old matcher but a different constructor signature. This should fix the compilation error.