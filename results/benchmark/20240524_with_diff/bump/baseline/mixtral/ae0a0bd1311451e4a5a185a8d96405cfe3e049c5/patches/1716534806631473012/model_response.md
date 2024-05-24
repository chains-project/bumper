Here's the fixed `shouldThrowExceptionWhenDigestIsAbsent` method:

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
        new StringStartsWith("Unexpected query")
    );
}
```

The change is replacing `StringContains` with `StringStartsWith` since the constructor signature has changed in the new library version.