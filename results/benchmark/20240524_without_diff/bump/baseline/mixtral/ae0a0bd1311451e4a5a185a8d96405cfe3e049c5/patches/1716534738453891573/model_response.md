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
        new StringStartsWith("Unexpected query") // changed to use StringStartsWith instead of StringContains
    );
}
```

In the new library version, the `StringContains` constructor no longer accepts a `boolean` argument. Instead, you can use the `StringStartsWith` matcher to check if the message starts with the expected string. This should fix the error and allow the test to pass.