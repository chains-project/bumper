```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    String exceptionMessage = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    ).getMessage();
    MatcherAssert.assertThat(exceptionMessage, CoreMatchers.containsString("Unexpected query"));
}
```