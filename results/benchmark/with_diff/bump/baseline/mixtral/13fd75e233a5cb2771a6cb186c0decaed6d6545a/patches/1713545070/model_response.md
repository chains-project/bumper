Here's a possible patch for the failing method:

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

* Replace `StringContains` with `StringStartsWith` for the first condition of `MatcherAssert.assertThat` in the `MatcherAssert.assertThat` statement.
* Remove the `true` parameter from `StringContains` constructor.
* Replace `InvalidTagNameException` with `exception` in the `MatcherAssert.assertThat` statement.

These changes are necessary because the `StringContains` constructor has changed its signature in the new version and now requires only one argument.