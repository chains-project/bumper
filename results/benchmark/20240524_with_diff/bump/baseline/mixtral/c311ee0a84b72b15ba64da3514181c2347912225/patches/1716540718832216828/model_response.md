Here is the proposed patch:
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
            ).getMessage(),
            stringContains
        );
    }
```
In this patch, I created a variable `stringContains` to hold the expected message, and moved its creation outside of the `StringContains` constructor call. This allows us to pass a single argument to the constructor, which is required by the new version of the library.