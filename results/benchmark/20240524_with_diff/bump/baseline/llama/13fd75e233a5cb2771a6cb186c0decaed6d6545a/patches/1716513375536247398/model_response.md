```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    );
    MatcherAssert.assertThat(throwable.getMessage(), CoreMatchers.containsString("Unexpected query"));
}
```