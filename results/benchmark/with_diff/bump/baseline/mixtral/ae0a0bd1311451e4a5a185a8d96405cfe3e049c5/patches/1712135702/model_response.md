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
        ).getMessage(),
        stringContains
    );
}
```
The changes I made are:

* I created a variable `stringContains` to store the `StringContains` matcher, which takes a single argument.
* I moved the creation of the `StringContains` matcher inside the lambda function passed to `Assertions.assertThrows`.
* I added a `return false;` statement at the end of the lambda function, to make it return a value. This is required because the lambda function must have a return type of `boolean`, to match the expected type of the `Assertions.assertThrows` method.

I hope this helps! Let me know if you have any questions.