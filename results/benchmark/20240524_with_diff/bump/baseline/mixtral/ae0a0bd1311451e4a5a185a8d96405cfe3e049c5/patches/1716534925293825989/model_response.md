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
The changes I made are:

* I created a local variable `stringContains` to store the `StringContains` matcher, instead of passing it directly to `MatcherAssert.assertThat()`.
* I moved the creation of the `IllegalStateException` inside a lambda expression, so that it can be caught and used in the `MatcherAssert.assertThat()` method.
* I added a `return false;` statement inside the lambda expression, so that it has a return value. This is required by the new version of the library, which expects the `MatcherAssert.assertThat()` method to have a non-void return type.

I hope this helps! Let me know if you have any other questions.