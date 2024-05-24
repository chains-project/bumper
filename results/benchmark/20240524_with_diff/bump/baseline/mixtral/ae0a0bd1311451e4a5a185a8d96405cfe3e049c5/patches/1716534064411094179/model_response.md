Here is the proposed patch:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    StringContains stringContains = StringContains.containsString("Unexpected query");
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
        stringContains
    );
}
```
Explanation:

The error message indicates that the `StringContains` constructor is expecting a single argument of type `String`, but it is receiving two arguments: a `boolean` and a `String`.

To fix the error, we can create a variable for the `StringContains` matcher, and pass a single argument of type `String` to its constructor.

This way, the code will comply with the new library version and the test should pass.