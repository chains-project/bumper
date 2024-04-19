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
            ).digest()
        ).getMessage(),
        new StringStartsWith("Unexpected query") // use StringStartsWith instead of StringContains
    );
}
```

In the new version of the library, the `StringContains` constructor has changed its signature and now requires only one argument, a `String`. To fix the error, you can replace `StringContains` with `StringStartsWith`, which has a similar functionality and accepts a single `String` argument. This should allow the code to compile and pass the test.