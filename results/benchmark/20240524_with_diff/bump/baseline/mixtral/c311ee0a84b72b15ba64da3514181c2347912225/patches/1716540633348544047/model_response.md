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
The changes I made are:

* I created a variable `stringContains` to store the `StringContains` matcher and used it in the `assertThat` method.
* I added a lambda expression to the `assertThrows` method to return `false` and avoid the compilation error.