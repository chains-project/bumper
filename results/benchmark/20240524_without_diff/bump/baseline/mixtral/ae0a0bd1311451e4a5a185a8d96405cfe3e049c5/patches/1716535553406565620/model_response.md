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
        new StringContains("Unexpected query")
    );
}
```
The issue was caused by passing two arguments to the `StringContains` constructor, whereas it only expects one argument. I have removed the `false` argument to resolve the error.