Here is a fixed version of the code that should resolve the error:

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
        new StringStartsWith("Unexpected query") // changed to use StringStartsWith instead of StringContains
    );
}
```

The error is caused by the fact that the `StringContains` matcher has been changed to require only a single argument, whereas the previous version accepted two arguments (a boolean and a string). To fix the error, we can replace the use of `StringContains` with `StringStartsWith`, which accepts a single string argument. This will allow the code to compile and run successfully with the new version of the library.