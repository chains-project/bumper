Here is a proposed patch for the failing client code:
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
The error message indicates that the `StringContains` constructor is expecting a single argument, but is receiving two arguments instead. To fix this issue, I have replaced `StringContains` with `StringStartsWith`, which only requires a single argument. This should resolve the error and allow the test to pass.