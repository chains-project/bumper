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

In the updated code, I created a separate variable `stringContains` for the `new StringContains("Unexpected query")` call, and passed it as an argument to `MatcherAssert.assertThat()` instead of passing the boolean value `false`. This way, the code now uses the correct version of the `StringContains` constructor.