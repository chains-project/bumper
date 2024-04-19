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
            )
        ).getMessage(),
        new StringStartsWith("Unexpected query") // use StringStartsWith instead of StringContains
    );
}
```
In the new library version, the `StringContains` constructor has changed its signature and now requires only one argument instead of two. Therefore, we need to replace `StringContains` with `StringStartsWith` to make the code compatible with the new library version.

Note that this patch assumes that the error message of the `IllegalStateException` starts with the substring "Unexpected query". If this assumption is not correct, then the test may fail. In that case, you may need to modify the argument of `StringStartsWith` accordingly.