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
            )
        ).getMessage(),
        new StringStartsWith("Unexpected query") // using StringStartsWith instead of StringContains
    );
}
```
The patch changes the `StringContains` matcher to a `StringStartsWith` matcher, since the former now requires a single string argument instead of a boolean and a string. This change should allow the test to compile and pass with the updated library version.