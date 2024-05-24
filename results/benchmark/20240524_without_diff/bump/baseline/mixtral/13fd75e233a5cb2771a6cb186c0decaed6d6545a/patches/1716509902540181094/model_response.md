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
The failure is caused by a change in the `StringContains` matcher of the Hamcrest library. In the new library version, the `StringContains` constructor no longer accepts a `boolean` parameter. Instead, you can use the `StringStartsWith` matcher, which accepts a `String` parameter.

In this patch, I replaced the `StringContains` matcher with the `StringStartsWith` matcher and updated the constructor argument accordingly. This change preserves the original test intent while using the new library version.