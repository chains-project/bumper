Here's a fixed version of the method that should work with the new library version:

```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    ".0",
    "*",
    "\u00ea",
    "-my-tag",
    //@checkstyle LineLengthCheck (1 line)
    "012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678"
})
void shouldFailToGetValueWhenInvalid(final String original) {
    final Matcher<String> containsMsg = new StringContains(original);
    final Matcher<Throwable> invalidTagMsg = new ArgumentMatchers.<Throwable>allOf(
        new ArgumentMatchers.<Throwable>hasMessage(new IsEqual<>("Invalid tag")),
        containsMsg
    );
    final Tag.Valid tag = new Tag.Valid(original);
    Assertions.assertThrows(InvalidTagNameException.class, () -> tag.value(), invalidTagMsg);
}
```
The changes made include:

* Using `new ArgumentMatchers.<Throwable>allOf` and `new ArgumentMatchers.<Throwable>hasMessage` to create the `Matcher` instances instead of `new AllOf` and `new StringContains`.
* Using a lambda expression `() -> tag.value()` with `Assertions.assertThrows` instead of passing `tag::value` as an argument.
* Creating separate `Matcher` variables for readability.

This version of the method should work with the new library version and pass the same tests as the original version.