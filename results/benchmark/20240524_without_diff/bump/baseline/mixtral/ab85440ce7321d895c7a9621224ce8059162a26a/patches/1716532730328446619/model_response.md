Here's a possible patch for the failing client code:
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
        new StringStartsWith("Unexpected query") // replace 'StringContains' with 'StringStartsWith'
    );
}
```
The failure is caused by a change in the Hamcrest library, where the `StringContains` matcher now requires only a single argument. To fix the failure, we can replace the `StringContains` matcher with a new matcher `StringStartsWith`, which has the same behavior as the old `StringContains` matcher.

Note that we cannot use the `StringContains` matcher with a single argument, as it is no longer supported by the new library version.