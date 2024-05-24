Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains ignore = false; // create a variable for the ignored argument
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
The change consists of creating a variable `ignore` for the unused argument of the `StringContains` constructor, which now only takes one argument. This allows the code to compile with the new version of the library.