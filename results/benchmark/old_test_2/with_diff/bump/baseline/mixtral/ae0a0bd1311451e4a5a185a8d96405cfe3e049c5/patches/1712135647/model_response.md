Here's a possible patch to fix the error:

```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains ignore = null;
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

The change here is to create a variable `ignore` of type `StringContains` and initialize it to `null`. This is necessary because the constructor for `StringContains` now requires only one argument, but the original code was passing two arguments. By introducing the `ignore` variable, we can remove the second argument and the error should be resolved.