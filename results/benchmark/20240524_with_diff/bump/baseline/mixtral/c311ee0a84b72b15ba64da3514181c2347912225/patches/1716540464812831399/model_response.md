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
        new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
    );
}
```

In the new library version, the `StringContains` matcher has been changed to require only a single argument, whereas in the previous version it allowed for two arguments (one of which was a boolean flag indicating whether the match should be case-sensitive). In this patch, I have replaced the `StringContains` matcher with the `StringStartsWith` matcher, which checks whether a string starts with a given prefix. This matcher only requires a single argument, so it is compatible with the new library version.

I hope this helps! Let me know if you have any questions or if you would like me to make any further changes.