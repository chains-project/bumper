Here's the fixed version of the code:

```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    StringContains stringContains = StringContains.containsString("Unexpected query");
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
        stringContains
    );
}
```

In the original code, the `StringContains` constructor was being called with two arguments, but it only accepts one argument. I've created a separate variable `stringContains` to hold the `StringContains` instance, which should fix the error.