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
            )
        ).getMessage(),
        new StringStartsWith("Unexpected query")
    );
}
```
The failure is caused by a change in the `StringContains` constructor, which now requires only one argument instead of two. To fix the failure, we can replace `new StringContains(false, "Unexpected query")` with `new StringStartsWith("Unexpected query")`. This ensures that the test passes even with the updated library version.