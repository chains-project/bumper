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
In this patch, I created a variable `ignore` to hold the `StringContains` matcher, and moved the `new StringContains` call outside of the `MatcherAssert.assertThat` method call. This way, the `StringContains` constructor can be called with the correct number of arguments. I also added a new `StringContains` matcher to the `MatcherAssert.assertThat` method call to check the exception message.

Note that the `ignore` variable is not actually used in the code, so it can be renamed to something more meaningful if desired.