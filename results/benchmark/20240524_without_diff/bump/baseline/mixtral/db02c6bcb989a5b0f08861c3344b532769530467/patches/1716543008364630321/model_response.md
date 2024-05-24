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
        new StringStartsWith("Unexpected query")
    );
}
```
The change made is to replace the `StringContains` matcher with the `StringStartsWith` matcher. This is because the constructor for `StringContains` now requires a single string argument instead of a boolean and a string. By using `StringStartsWith`, the test still checks that the message starts with "Unexpected query", but the test will now compile with the new library version.