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
            new StringStartsWith(new IsEqual<>("Invalid tag")),
            new StringContains(original)
        )
    );
}
```

The changes I made are:

1. Replaced the `StringContains` matcher with `StringStartsWith` and `StringContains` to match the new library version.
2. Removed the `true` and `false` arguments from the `StringContains` matcher, as they are not supported anymore.
3. Updated the imports if necessary.

Please note that the `StringStartsWith` matcher is used here instead of the `StringContains` matcher with the `true` argument, as the new library version does not support the latter.