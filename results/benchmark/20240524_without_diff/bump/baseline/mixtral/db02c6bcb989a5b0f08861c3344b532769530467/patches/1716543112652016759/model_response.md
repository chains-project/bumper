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
        ),
        new StringContains("Unexpected query")
    );
}
```
In this patch, I created a new variable `ignore` of type `StringContains` and initialized it with the value `false`. This allows us to use the `StringContains` constructor that takes a single `String` argument.

I then wrapped the creation of the `UploadEntity.Request` object in a lambda expression, which is passed to the `Assertions.assertThrows` method. This allows us to use the `StringContains` constructor with a single `String` argument.

Finally, I changed the argument of the `new StringContains` constructor to remove the `false` parameter, so that it only takes a single `String` argument.

This patch should fix the error and allow the test to pass.