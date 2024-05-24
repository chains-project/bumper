Here is a fixed version of the failing method using the new library version:

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
        new StringContains("Unexpected query")
    );
}
```

The issue was caused by passing an incorrect number of arguments to the `StringContains` constructor. The new version of the library only accepts a single `String` argument.