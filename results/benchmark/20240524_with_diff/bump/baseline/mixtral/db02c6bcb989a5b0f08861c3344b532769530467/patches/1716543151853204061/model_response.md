Here's the proposed patch to fix the error:

```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> new UploadEntity.Request(
                new RequestLine(
                    RqMethod.PUT,
                    "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                ).toString()
            ).digest()
        ),
        new StringContains("Unexpected query") // removed 'false' argument
    );
}
```

The issue is caused by passing an unnecessary boolean argument to the `StringContains` constructor, which was changed in the new library version. The patch removes the unnecessary argument to fix the error.