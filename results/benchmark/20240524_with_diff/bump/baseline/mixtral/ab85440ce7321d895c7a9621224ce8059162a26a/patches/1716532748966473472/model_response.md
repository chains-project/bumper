Here's a fixed version of the failing method that should work with the updated library:

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

The only change I made was to remove the `false` argument in the `StringContains` constructor. It looks like the updated library version no longer requires this argument.