Here's a proposed patch for the failing client code:

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
        ).getMessage(),
        new StringContains("Unexpected query")
    );
}
```

The only change made here is to remove the `false` argument from the `StringContains` constructor. This is because the `StringContains` constructor with a single `String` argument is the correct one to use here, and the `boolean` argument was added in a later version of the library. This change should allow the code to compile and run successfully with the updated library version.