Here's the updated method with the required changes:

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
            new AllOf<>(
                    Arrays.asList(
                            new StringStartsWith<>("Invalid tag"),
                            new StringContains<>(original)
                    )
            )
    );
}
```

The changes include:

1. Removed the `true` argument from the `StringContains` constructor, as it is no longer required in the new version of the library.
2. Replaced `StringContains` with `StringStartsWith` for the first string matcher, as the error message should start with "Invalid tag".
3. Added a variable for the `InvalidTagNameException` to make the code easier to read.