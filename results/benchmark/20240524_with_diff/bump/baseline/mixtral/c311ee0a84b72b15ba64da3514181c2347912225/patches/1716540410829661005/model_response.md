Here's the proposed patch:

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
              return null;
            }
        ).getMessage(),
        stringContains
    );
}
```

I created a local variable `stringContains` for the `StringContains` matcher, so it can be reused without passing the `false` argument. This way, the code is compatible with the new library version.