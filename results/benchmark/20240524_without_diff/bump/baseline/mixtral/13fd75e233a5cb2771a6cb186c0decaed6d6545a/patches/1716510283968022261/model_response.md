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
In the original code, the `StringContains` constructor was being called with two arguments, but the updated library version only accepts one argument. I have updated the code to only pass one argument to the `StringContains` constructor.