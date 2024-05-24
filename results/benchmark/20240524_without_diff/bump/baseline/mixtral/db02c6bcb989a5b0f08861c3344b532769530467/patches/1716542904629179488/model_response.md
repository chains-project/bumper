Here's the proposed patch:

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
        new StringStartsWith("Unexpected query") // modified line
    );
}
```

The change is in the `StringContains` matcher, which has been replaced with `StringStartsWith`. The error message indicates that the `StringContains` constructor now requires a single string argument, while it previously accepted a boolean and a string. This change might have been introduced in the updated library version. To fix the issue, `StringStartsWith` is used instead, which only requires a single string argument.