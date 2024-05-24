Here's the fixed `shouldFailToGetValueWhenInvalid` method:

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
                new StringStartsWith("Invalid tag"),
                new StringContains(original)
            )
        )
    );
}
```

The fix includes changing the `StringContains` matcher to `StringStartsWith` and removing the `true` argument from it. This change is required because the updated library version no longer supports the `StringContains` constructor with two arguments. Instead, it uses a single argument for the expected substring. The `StringStartsWith` matcher is used to ensure that the error message starts with the "Invalid tag" string.