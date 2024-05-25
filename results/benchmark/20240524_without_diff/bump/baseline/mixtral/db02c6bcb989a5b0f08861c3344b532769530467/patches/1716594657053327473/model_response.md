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
        new StringContains("Unexpected query")
    );
}
```
The only change I made is to replace `new StringContains(false, "Unexpected query")` with `new StringContains("Unexpected query")`. This is because the constructor `StringContains(String)` was added in a newer version of Hamcrest, and it is a more convenient way to create a `StringContains` matcher. The `boolean` argument was deprecated and removed in newer versions.

Note that this patch assumes that the version of Hamcrest being used is at least 1.3, which is when the `StringContains(String)` constructor was added. If a lower version of Hamcrest is being used, then the patch would need to be different.