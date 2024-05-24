Here is a possible patch for the failing code:
```java
@Test
void shouldThrowExceptionWhenDigestIsAbsent() {
    MatcherAssert.assertThat(
        Assertions.assertThrows(
            IllegalStateException.class,
            () -> {
                StringContains ignore = new StringContains(false, "Unexpected query");
                new UploadEntity.Request(
                    new RequestLine(
                        RqMethod.PUT,
                        "/v2/my-repo/blobs/uploads/123-abc?what=nothing"
                    ).toString()
                ).digest();
            }
        ),
        new StringContains("Unexpected query")
    );
}
```
The changes I made are as follows:

* I created a new variable `ignore` of type `StringContains` and initialized it with the arguments `(false, "Unexpected query")`. This is because the constructor of `StringContains` now requires only one argument, and the second argument is being deprecated.
* I moved the creation of `ignore` inside the lambda expression `() -> { ... }` passed to `Assertions.assertThrows()`. This is because the error message suggests that the second argument of `StringContains` is no longer required and is being deprecated.
* I changed the argument of the `StringContains` matcher passed to `MatcherAssert.assertThat()` to `"Unexpected query"`. This is because the constructor of `StringContains` now requires only one argument, and the second argument is being deprecated.

I hope this helps! Let me know if you have any questions.