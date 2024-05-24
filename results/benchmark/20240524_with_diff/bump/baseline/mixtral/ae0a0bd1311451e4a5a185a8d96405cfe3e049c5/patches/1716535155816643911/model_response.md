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

In the updated code, I created a `StringContains` variable `stringContains` outside of the `assertThat` method and passed it as an argument. This way, the `assertThat` method only receives one argument, which is the expected format for the `StringContains` constructor.