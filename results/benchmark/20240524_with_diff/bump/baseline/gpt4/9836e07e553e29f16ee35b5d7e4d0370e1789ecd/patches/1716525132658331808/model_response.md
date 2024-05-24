```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    final IllegalStateException e = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    );
    MatcherAssert.assertThat(
        e.getMessage(),
        Matchers.containsString("Unexpected query")
    );
}
```