Here is the fixed version of the failing method:

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

The only change made is in the `new StringContains` constructor call, where the `false` argument has been removed. This is because the constructor for `StringContains` no longer accepts a boolean argument in the new library version.