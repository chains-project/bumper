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
        ),
        stringContains
    );
}
```

I created a variable `stringContains` to store the `StringContains` matcher and reused it in the `assertThat` method. This way, we avoid passing the `boolean` parameter to `StringContains`.