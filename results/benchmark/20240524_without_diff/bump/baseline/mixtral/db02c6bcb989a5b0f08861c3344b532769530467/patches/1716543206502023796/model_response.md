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
            new StringStartsWith("Unexpected query") // change here
        );
    }
```
The failure is caused by the incorrect usage of the `StringContains` matcher. It expects only one argument, but it is called with two arguments. I have replaced it with the `StringStartsWith` matcher, which only takes one argument. This should fix the error.