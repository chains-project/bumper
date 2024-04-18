Here is a patch that you can apply to the failing client code:
```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    ".0",
    "*",
    "\u00ea",
    "-my-tag",
    "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678"
})
void shouldFailToGetValueWhenInvalid(String original) {
    Matcher<String> containsMsg = new StringContains(original);
    Matcher<Throwable> invalidTagMsg = ArgumentMatchers.<Throwable>allOf(
        ArgumentMatchers.<Throwable>hasMessage(new IsEqual<>("Invalid tag")),
        containsMsg
    );
    Tag.Valid tag = new Tag.Valid(original);
    Assertions.assertThrows(InvalidTagNameException.class, () -> {
        tag.value();
    }, invalidTagMsg);
}
```
I added a pair of curly braces around the statement `tag.value();` to fix the error message "[ERROR] /docker-adapter/src/test/java/com/artipie/docker/TagValidTest.java:[56,9] not a statement".

Note that I did not use any of the removed library methods identified with `--`, and I did not use any added library methods identified with `++`. I only made changes to the client code.

I hope this helps! Let me know if you have any questions.