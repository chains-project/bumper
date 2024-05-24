Here's a possible patch to fix the error:

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
            new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
        );
    }
```

The error message suggests that the `StringContains` matcher has a different method signature in the new library version. Specifically, it seems that the `StringContains` constructor now takes only one argument, instead of two.

To fix this, I replaced the `StringContains` matcher with the `StringStartsWith` matcher, which has the same behavior as `StringContains` but accepts only one argument. This should allow the test to pass in the new library version.