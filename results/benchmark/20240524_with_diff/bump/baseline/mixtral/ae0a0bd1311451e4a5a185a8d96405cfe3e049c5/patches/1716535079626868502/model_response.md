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
            new StringStartsWith("Unexpected query")
        );
    }
```
The failure was caused by the incorrect usage of the `StringContains` matcher. Instead of passing a boolean flag as the first argument, the matcher should be instantiated with a string argument. In this case, I have replaced the `StringContains` matcher with the `StringStartsWith` matcher, which checks if a string starts with a given substring. This should fix the error and make the test pass.