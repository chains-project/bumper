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
            ).digest()
        ).getMessage(),
        new StringStartsWith("Unexpected query") // replace StringContains with StringStartsWith
    );
}
```

The `StringContains` matcher has been replaced with the `StringStartsWith` matcher, which only requires a single argument. This should resolve the error message related to the mismatch in the number of arguments provided to the `StringContains` constructor.