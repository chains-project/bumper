```
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    String message = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    ).getMessage();
    MatcherAssert.assertThat(message, Matchers.containsString("Unexpected query"));
}
```