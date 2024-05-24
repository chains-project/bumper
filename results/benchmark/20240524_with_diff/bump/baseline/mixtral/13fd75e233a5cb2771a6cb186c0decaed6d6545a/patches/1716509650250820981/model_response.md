Here's the proposed patch to fix the error:

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
                    new StringContains(original)
                )
            )
        );
    }
```

The changes made are:

1. Replaced `new StringContains(true, "Invalid tag")` with `new StringContains("Invalid tag")`.
2. Replaced `new StringContains(false, original)` with `new StringContains(original)`.

The reason for these changes is that the `StringContains` constructor signature has changed and now only accepts a single argument.