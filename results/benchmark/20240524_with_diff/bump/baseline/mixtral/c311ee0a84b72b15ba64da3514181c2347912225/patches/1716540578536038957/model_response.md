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
              return null; // avoid "variable might not have been initialized" error
            }
        ).getMessage(),
        stringContains
    );
}
```

The patch replaces the `new StringContains(false, "Unexpected query")` with a local variable `stringContains` to fix the error caused by the change in the library version.