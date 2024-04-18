Here's a patch that should fix the error:

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
    final Matcher<Throwable> invalidTagMsg = ArgumentMatchers.<Throwable>allOf(
        ArgumentMatchers.<Throwable>hasMessage(new IsEqual<>("Invalid tag")),
        containsMsg
    );
    InvalidTagNameException exception = null;
    try {
        new Tag.Valid(original).value();
    } catch (InvalidTagNameException e) {
        exception = e;
    }
    Assertions.assertThrows(InvalidTagNameException.class, () -> {
        if (exception != null) {
            throw exception;
        }
    }, invalidTagMsg);
}
```

The patch wraps the creation of the `Tag.Valid` object and its value method call in a try-catch block. This allows the `Assertions.assertThrows` method to work as expected without throwing a compilation error. The caught exception is then re-thrown in the lambda expression passed to `Assertions.assertThrows`.