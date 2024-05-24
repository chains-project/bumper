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
The only change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which only takes a single string argument. This is because the `StringContains` matcher in the new library version no longer accepts a boolean argument.

Note that this patch assumes that the error message of the `IllegalStateException` thrown by the `UploadEntity.Request` constructor starts with the string "Unexpected query". If this assumption is incorrect, then the test may fail even after applying the patch. In this case, you may need to modify the matcher or the expected error message accordingly.