```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    String expectedMessage = "Unexpected query";
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> new UploadEntity.Request(
                new RequestLine(
                    RqMethod.PUT,
                    "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                ).toString()
            ).digest()
        ).getMessage(),
        CoreMatchers.containsString(expectedMessage)
    );
}
```