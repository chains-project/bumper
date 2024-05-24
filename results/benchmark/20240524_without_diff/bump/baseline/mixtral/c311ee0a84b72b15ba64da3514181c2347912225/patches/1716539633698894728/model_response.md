Here is a fixed version of the code that should work with the updated library:

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

The issue is caused by the change in the `StringContains` constructor. In the updated library version, the constructor now takes only one argument (a `String`), whereas in the previous version, it took two arguments (a `boolean` and a `String`).

To fix the issue, you can use the `StringStartsWith` matcher instead of `StringContains`. This matcher checks if a string starts with a given substring. In this case, it checks if the exception message starts with the substring "Unexpected query".