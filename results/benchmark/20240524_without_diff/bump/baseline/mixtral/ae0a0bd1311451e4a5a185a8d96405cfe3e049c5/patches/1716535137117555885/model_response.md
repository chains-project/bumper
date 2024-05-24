Here's the proposed patch for the failing client code:

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
        new StringStartsWith("Unexpected query") // using StringStartsWith instead of StringContains
    );
}
```

This patch replaces the `StringContains` matcher with the `StringStartsWith` matcher, which accepts a single argument, making the code compatible with the new library version.