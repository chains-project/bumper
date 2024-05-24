Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
              StringContains ignore = new StringContains(false, "Unexpected query");
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
In this patch, I created a new variable `ignore` to hold the `StringContains` matcher with the `false` flag, which is no longer accepted by the constructor. Then, I moved the `new UploadEntity.Request` call and the `digest` method call inside a lambda expression, so that the `MatcherAssert` call will only receive the `IllegalStateException` and the expected `StringContains` matcher.

Note: This patch assumes that the `StringContains` constructor with a single `String` argument is still available in the new library version. If this is not the case, you may need to adjust the patch accordingly.