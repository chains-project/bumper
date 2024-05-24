```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    IllegalStateException exception = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    );
    MatcherAssert.assertThat(
        exception.getMessage(),
        CoreMatchers.containsString("Unexpected query")
    );
}
```