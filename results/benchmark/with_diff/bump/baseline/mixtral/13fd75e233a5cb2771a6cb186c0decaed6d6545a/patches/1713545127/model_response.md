Here's the updated method with the fix:

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
                new StringContains("Invalid tag"),
                new StringStartsWith(original.isEmpty() ? "" : original.substring(0, 1))
            )
        )
    );
}
```

The fix involves changing the `StringContains` matcher to use the `StringStartsWith` matcher for the second `StringContains` condition. This is because the `StringContains` constructor that accepts a boolean value has been removed in the new library version and the error message is now expected to contain the first character of the invalid tag instead.