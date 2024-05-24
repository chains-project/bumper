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
            ).digest()
        ),
        new StringContains("Unexpected query")
    );
}
```
The only change I made is to remove the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor that takes a `boolean` argument was removed in the new library version. The `StringContains` constructor that takes a single `String` argument is still available, so I used that instead. This should allow the code to compile and run correctly with the new library version.