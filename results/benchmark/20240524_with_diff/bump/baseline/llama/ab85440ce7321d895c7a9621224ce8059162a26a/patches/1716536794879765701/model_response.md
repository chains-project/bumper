```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    String errorMessage = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    ).getMessage();
    MatcherAssert.assertThat(errorMessage, Matchers.containsString("Unexpected query"));
}
```