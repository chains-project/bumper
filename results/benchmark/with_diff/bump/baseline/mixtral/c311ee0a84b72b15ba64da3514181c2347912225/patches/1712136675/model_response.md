Here's a suggested patch for the failing code:

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

The only change made is to wrap the call to `tag.value()` in a lambda expression, which is required by `Assertions.assertThrows` in the new version of the library.