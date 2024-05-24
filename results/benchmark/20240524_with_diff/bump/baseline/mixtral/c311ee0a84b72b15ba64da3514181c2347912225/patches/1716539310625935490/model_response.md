Here's the updated `shouldFailToGetValueWhenInvalid` method that should fix the error:

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
            Arrays.asList(
                new StringStartsWith("Invalid tag"),
                new StringContains(original)
            )
        )
    );
}
```

The changes made are:

1. Removed the `true` argument from the `StringContains` constructor, as it's no longer needed in the new library version.
2. Changed the `StringContains` constructor to use a single argument, the `original` string, to match the new library version.
3. Replaced the `StringContains` constructor with a `StringStartsWith` constructor to ensure the error message starts with "Invalid tag".

These changes should fix the error and make the code compatible with the new library version.