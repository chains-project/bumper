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
In the updated code, I have created a `StringContains` variable `stringContains` and passed it to the `MatcherAssert.assertThat` method. This way, the `StringContains` constructor takes only one argument, which resolves the error.