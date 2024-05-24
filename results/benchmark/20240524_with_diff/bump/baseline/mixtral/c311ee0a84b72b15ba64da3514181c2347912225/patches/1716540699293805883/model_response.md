Here is the proposed patch:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains contains = new StringContains("Unexpected query");
                new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString()
                ).digest();
                return false;
            }
        ).getMessage(),
        contains
    );
}
```
In the updated code, I created a variable `contains` to store the `StringContains` matcher and used it in the `assertThat` method. This way, the `StringContains` constructor is called with the correct number of arguments, fixing the error.