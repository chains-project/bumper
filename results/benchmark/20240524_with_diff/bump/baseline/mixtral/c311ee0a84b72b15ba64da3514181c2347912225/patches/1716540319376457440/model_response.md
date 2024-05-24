Here is a possible patch for the failing client code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains stringContains = new StringContains("Unexpected query");
                new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString()
                ).digest();
                return false;
            }
        ),
        stringContains
    );
}
```
This patch creates a `StringContains` object before the lambda expression, and uses it as the argument to `MatcherAssert.assertThat()`. This allows the `StringContains` constructor to be called with a single argument, as required by the new library version.