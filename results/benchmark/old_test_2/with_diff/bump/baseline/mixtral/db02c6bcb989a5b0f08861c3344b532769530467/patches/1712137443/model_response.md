Here's a possible patch for the given code:

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
                    new StringContains("Invalid tag"),
                    new StringStartsWith("Invalid tag"),
                    new StringEndsWith(original)
                )
            )
        );
    }
```

The changes made are:

1. Removed the `true` argument from the `StringContains` constructor.
2. Added `StringStartsWith` and `StringEndsWith` matchers to replace the functionality of the second argument in the `StringContains` constructor.

These changes should make the code compatible with the updated library version.