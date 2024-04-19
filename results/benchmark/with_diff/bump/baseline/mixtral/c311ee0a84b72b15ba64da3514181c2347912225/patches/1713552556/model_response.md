Here is a patch that you can apply to fix the error:

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
        new StringStartsWith("Unexpected query") // changed here
    );
}
```

The error message is caused by the fact that the constructor for `StringContains` has changed in the new library version. Instead of passing a boolean value as the first argument, you can use the `StringStartsWith` matcher instead. This will achieve the same functionality and will not cause any errors.