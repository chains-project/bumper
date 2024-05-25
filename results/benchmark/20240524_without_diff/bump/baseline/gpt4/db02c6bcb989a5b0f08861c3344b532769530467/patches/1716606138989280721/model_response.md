```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    String expectedMessage = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new UploadEntity.Request(
            new RequestLine(
                RqMethod.PUT,
                "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
            ).toString()
        ).digest()
    ).getMessage();
    MatcherAssert.assertThat(
        expectedMessage,
        CoreMatchers.containsString("Unexpected query")
    );
}
```