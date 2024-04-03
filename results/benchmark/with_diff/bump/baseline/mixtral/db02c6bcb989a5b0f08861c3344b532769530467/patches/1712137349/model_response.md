Here's the fixed version of the `shouldFailToGetValueWhenInvalid` method:

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
    final Tag.Valid tag = new Tag.Valid(original);
    MatcherAssert.assertThat(tag.valid(), new IsEqual<>(false));
    final InvalidTagNameException e = Assertions.assertThrows(
        InvalidTagNameException.class,
        tag::value
    );
    MatcherAssert.assertThat(
        e.getMessage(),
        new AllOf(
            new ArrayContaining(new StringContains("Invalid tag")),
            not(new StringContains(original))
        )
    );
}
```

In the original code, the `StringContains` constructor was being called incorrectly with two arguments, while it accepts only one. I've replaced the `StringContains` matcher with `ArrayContaining` and `not` matchers to achieve the same functionality.

The `ArrayContaining` matcher checks if the actual value contains the expected substring, and the `not` matcher negates the matcher it wraps. This way, we check if the message contains "Invalid tag" but doesn't contain the original input string.