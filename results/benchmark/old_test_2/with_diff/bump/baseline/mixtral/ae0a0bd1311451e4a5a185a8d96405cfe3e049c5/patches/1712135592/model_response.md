Here's a possible patch for the failing client code:

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
        new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
    );
}
```

In this patch, I replaced the `StringContains` matcher with `StringStartsWith`. This is because the constructor signature of `StringContains` has changed in the new library version, requiring a single string argument instead of a boolean and a string. The `StringStartsWith` matcher, on the other hand, has a constructor that takes a single string argument and can be used to achieve similar functionality.