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
The only change I made is to replace the `StringContains` matcher with the `StringStartsWith` matcher, which has a different constructor signature and should be compatible with the new version of the library. This matcher checks if the given string starts with the specified prefix, which is sufficient for the purpose of this test.