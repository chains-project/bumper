Here's the proposed patch for the failing method:

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

The changes made are:

1. Replace `new StringContains(true, "Invalid tag")` with `new StringStartsWith("Invalid tag")`. This is because the constructor `StringContains` no longer accepts a boolean parameter in the new library version.
2. Remove the `false` parameter from `new StringContains(false, original)`. This is because the constructor `StringContains` no longer accepts a boolean parameter in the new library version.

Note that I assumed that the `InvalidTagNameException` class has a `getMessage()` method that returns a `String` object. If this is not the case, you may need to adjust the code accordingly.