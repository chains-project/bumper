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

In the new library version, the `StringContains` constructor has changed its signature and now requires only one argument, instead of two. To fix the error, we can replace the `StringContains` constructor with the `StringStartsWith` constructor, which has a similar behavior. Note that the `StringStartsWith` constructor only checks if the actual string starts with the expected substring, instead of checking if it contains it. If you need to check if the actual string contains the expected substring, you can use the `StringContains` static method instead.