Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains ignore = false;
                return new UploadEntity.Request(
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
In this patch, I created a new variable `ignore` of type `StringContains` and initialized it to `false`. This allows us to use the `StringContains` constructor that takes a single `String` argument.

Then I wrapped the construction of `UploadEntity.Request` in a lambda expression, so that we can create the `StringContains` instance inside the lambda expression, but still throw the exception outside of it.

Finally, I changed the order of arguments of the second `MatcherAssert.assertThat` call, so that it matches the new signature of `StringContains` constructor.

This patch should fix the error and allow the test to pass with the new version of the library.