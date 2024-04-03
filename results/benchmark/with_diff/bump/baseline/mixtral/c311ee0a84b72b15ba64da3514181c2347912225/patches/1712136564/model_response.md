Here's a possible patch for the failing method:

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

The changes made are:

* Removed the `final` keyword from the `original` parameter.
* Wrapped the `tag.value()` call in a lambda expression to pass to `Assertions.assertThrows()`.

These changes should resolve the "not a statement" error and allow the test to compile and run with the updated library version.