Here is the proposed patch:
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
In this patch, I created a variable `stringContains` to store the `StringContains` matcher and passed it directly to `MatcherAssert.assertThat()` instead of creating a new `StringContains` instance directly in the method call. This way, the error caused by the incorrect number of arguments is resolved.