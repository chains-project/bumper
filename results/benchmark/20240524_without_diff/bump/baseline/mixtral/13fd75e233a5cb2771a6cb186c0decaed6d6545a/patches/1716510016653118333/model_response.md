Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains ignore = false;
                new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString()
                ).digest();
            }
        ).getMessage(),
        new StringContains("Unexpected query")
    );
}
```
I added a dummy variable `ignore` of type `StringContains` to satisfy the new signature of the `StringContains` constructor. This way, the test case should pass without modifying the behavior of the original code.