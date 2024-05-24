```java
@Test
    void shouldThrowExceptionWhenDigestIsAbsent() {
        // TODO: review this AI generated patch!
        MatcherAssert.assertThat(
            Assertions.assertThrows(
                IllegalStateException.class,
                () -> new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc"
                    ).toString()
                ).digest(),
            new StringContains(false, "Unexpected query")
        );
    }
```