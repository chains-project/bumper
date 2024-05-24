Here is the proposed patch:
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
            new StringContains("Unexpected query")
        );
    }
```
The only change made is in the `new StringContains` constructor, where the `false` argument has been removed. This is because the `StringContains` constructor with a boolean argument has been removed in the new library version.