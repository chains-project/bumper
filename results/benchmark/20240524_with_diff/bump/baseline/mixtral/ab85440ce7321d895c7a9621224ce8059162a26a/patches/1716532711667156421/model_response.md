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
        new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
    );
}
```
The error message suggests that the `StringContains` matcher constructor is being called with two arguments, while it only accepts one. The updated library version may have changed the behavior of the `StringContains` matcher.

To fix the error, we can replace the `StringContains` matcher with a different matcher that accepts two arguments. In this case, we can use the `StringStartsWith` matcher instead.

Note that we cannot be sure that this patch will work without testing it, as we do not know the exact behavior of the updated library version. However, this patch should at least resolve the compilation error.