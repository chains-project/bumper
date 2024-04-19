Here is a possible patch for the failing client code:

```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> new UploadEntity.Request(
                new RequestLine(
                    RqMethod.PUT,
                    "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                ).toString()
            )
        ).getMessage(),
        new StringStartsWith("Unexpected query") // use StringStartsWith instead of StringContains
    );
}
```

In the new library version, the `StringContains` constructor has changed its signature and now requires only one argument (a `String`), instead of two (a `boolean` and a `String`). Therefore, I replaced `StringContains` with `StringStartsWith`, which has the same functionality and accepts only one argument. This should fix the error and allow the test to pass.