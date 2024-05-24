Here's a suggested patch for the failing client code:

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

The only change made is to remove the `false` argument from the `StringContains` constructor. It seems that the `StringContains` constructor no longer accepts a boolean argument in the new library version, so we can simply remove it.