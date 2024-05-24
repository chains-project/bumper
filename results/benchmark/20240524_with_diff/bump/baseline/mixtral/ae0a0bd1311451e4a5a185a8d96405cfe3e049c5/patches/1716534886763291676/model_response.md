Here's a fixed version of the code that should resolve the error:

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
        ),
        new StringStartsWith("Unexpected query") // changed to use StringStartsWith instead of StringContains
    );
}
```

The error message indicates that the `StringContains` constructor is expecting a single argument (a string), but it's receiving two arguments (a boolean and a string). To fix this, we can replace `StringContains` with `StringStartsWith`, which only takes a single string argument. This should resolve the error and allow the code to compile and run successfully.