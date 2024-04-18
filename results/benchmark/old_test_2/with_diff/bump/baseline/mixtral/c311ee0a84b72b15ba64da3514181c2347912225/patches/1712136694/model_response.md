Here is a possible patch for the failing client code:
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
The patch removes the final keyword from the `original` parameter, and encloses the call to `tag.value()` in curly braces to make it a statement. These changes should fix the "not a statement" error.