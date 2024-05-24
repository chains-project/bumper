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
In this patch, I created a new variable `ignore` of type `StringContains` to hold the `StringContains` instance that was causing the error. I then moved the `StringContains` instance inside the lambda expression passed to `Assertions.assertThrows` and changed the expected message to a plain `StringContains` instance.

This patch should fix the error while preserving the original functionality of the test method.