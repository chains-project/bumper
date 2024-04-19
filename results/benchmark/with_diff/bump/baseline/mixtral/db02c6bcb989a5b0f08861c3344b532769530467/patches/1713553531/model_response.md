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
    final InvalidTagNameException exception = Assertions.assertThrows(
        InvalidTagNameException.class,
        tag::value
    );
    MatcherAssert.assertThat(
        exception.getMessage(),
        new AllOf<>(
            new StringContains(exception.getMessage(), "Invalid tag"),
            new StringContains(exception.getMessage(), original)
        )
    );
}
```

The change in the library version seems to have caused a problem with the `StringContains` constructor. To fix the issue, I replaced the `MatcherAssert.assertThat` call with a new `MatcherAssert.assertThat` call that uses `AllOf` with two separate `StringContains` matchers.

The first `StringContains` matcher checks if the message contains the substring "Invalid tag", while the second `StringContains` matcher checks if the message contains the original string.

This should resolve the compilation error and allow the test to pass.