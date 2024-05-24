Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains matcher = new StringContains("Unexpected query");
                new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString()
                ).digest();
                return false; // this is needed to satisfy the new StringContains constructor
            }
        ).getMessage(),
        matcher
    );
}
```
The changes I made are:

* I created a `matcher` variable to store the `StringContains` instance, so that it can be reused in the `MatcherAssert.assertThat` call.
* I added a dummy `return` statement inside the lambda expression passed to `Assertions.assertThrows`, to satisfy the new `StringContains` constructor which expects a second argument of type `boolean`.

These changes should fix the error and make the code compatible with the new library version.