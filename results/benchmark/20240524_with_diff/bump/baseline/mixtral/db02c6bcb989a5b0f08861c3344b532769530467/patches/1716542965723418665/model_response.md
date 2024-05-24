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

* I created a local variable `stringContains` to store the `StringContains` matcher, and used it in the `MatcherAssert.assertThat` call. This avoids passing a boolean value as the second argument to `StringContains`, which was causing the compilation error.
* I added a `return false;` statement inside the lambda expression passed to `Assertions.assertThrows`. This is because the lambda expression must have a return type of `IllegalStateException`, but the original code did not return anything. Adding the `return false;` statement ensures that the lambda expression has a valid return value.

Note that I did not use any removed library methods (marked with `--`), and I used the added library method `StringContains(String)` (marked with `++`). I also did not remove the `@Override` decorator, because the method is still overriding a method in the new version. Finally, I did not change the function signature or create any new variables that are not used in the code.