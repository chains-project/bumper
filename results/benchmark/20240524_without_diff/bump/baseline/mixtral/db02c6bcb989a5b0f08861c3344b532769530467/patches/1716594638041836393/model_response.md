Here's the proposed patch:

```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
              String query = "?what=nothing";
              String path = "/v2/my-repo/blobs/uploads/123-abc";
              UploadEntity.Request request = new UploadEntity.Request(
                  new RequestLine(
                      RqMethod.PUT,
                      path + query
                  ).toString()
              );
              request.digest();
              return null;
            }
        ).getMessage(),
        new StringContains(false, "Unexpected query")
    );
}
```

In this patch, I created a new variable `query` for the query string and `path` for the path string. I then concatenated them when creating the `RequestLine`. This way, the `toString()` method of `RequestLine` will not include the query string, and the `IllegalStateException` will be thrown as expected.