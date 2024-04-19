Here's the proposed patch to fix the error:

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
        new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
    );
}
```
In the original code, the `StringContains` matcher is used incorrectly with two arguments, while it only accepts one argument. In the updated code, I replaced `StringContains` with `StringStartsWith` which checks if a string starts with a specified substring. This should resolve the error.