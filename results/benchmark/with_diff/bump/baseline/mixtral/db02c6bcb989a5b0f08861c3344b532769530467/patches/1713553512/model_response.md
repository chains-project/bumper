Here's the updated `shouldFailToGetValueWhenInvalid` method that fixes the error:

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
    MatcherAssert.assertThat(exception.getMessage(), new AllOf(
        Arrays.asList(
            new StringStartsWith("Invalid tag"),
            new StringContains(original)
        )
    ));
}
```

The changes include:

1. Replacing the `StringContains` constructor with the `StringStartsWith` constructor and adding a new `StringContains` matcher to ensure the error message starts with "Invalid tag" and contains the original input.

This should fix the error related to the constructor of `StringContains` having a different number of arguments.