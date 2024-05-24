Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
              StringContains stringContains = new StringContains("Unexpected query");
              new UploadEntity.Request(
                  new RequestLine(
                      RqMethod.PUT,
                      "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                  ).toString()
              ).digest();
              return false;
            }
        ).getMessage(),
        stringContains
    );
}
```
In this patch, I created a variable `stringContains` to store the `StringContains` matcher, and used it in the `assertThat` method. This way, the `StringContains` constructor is called with the correct number of arguments, fixing the error.