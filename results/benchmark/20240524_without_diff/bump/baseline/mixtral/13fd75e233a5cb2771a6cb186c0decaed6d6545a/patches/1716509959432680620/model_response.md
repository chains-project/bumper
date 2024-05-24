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
In this patch, I created a new variable `ignore` of type `StringContains` and initialized it with the value `false`. This allows us to use the `StringContains` constructor that takes a single `String` argument, as required by the updated library version.

I also wrapped the creation of the `UploadEntity.Request` object in a lambda expression, which allows us to use the `ignore` variable in the same block.

Finally, I removed the `override` decorator from the method, as it is not overriding any method in the new version of the library.

This patch should fix the error and allow the test to pass with the updated library version.