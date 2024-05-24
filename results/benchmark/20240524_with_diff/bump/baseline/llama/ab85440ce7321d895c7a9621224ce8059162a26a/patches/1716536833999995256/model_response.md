```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    String expectedMessage = "Unexpected query";
    Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    );
    MatcherAssert.assertThat(throwable.getMessage(), CoreMatchers.containsString(expectedMessage));
}
```