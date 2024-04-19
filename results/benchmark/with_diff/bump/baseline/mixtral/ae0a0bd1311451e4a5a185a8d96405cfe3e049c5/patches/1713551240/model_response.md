Here is a possible patch for the failing client code:
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
        new StringStartsWith("Unexpected query") // use StringStartsWith instead of StringContains
    );
}
```
The patch replaces the `StringContains` matcher with the `StringStartsWith` matcher, which has the same semantics but a different constructor signature. This should fix the error caused by the updated library version.