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
            )
        ).getMessage(),
        new StringStartsWith("Unexpected query") // changed 'StringContains' to 'StringStartsWith'
    );
}
```

The failure is caused by a change in the `StringContains` constructor. The new version requires only one argument, while the old version accepts two arguments. I replaced `StringContains` with `StringStartsWith` to fix the issue.