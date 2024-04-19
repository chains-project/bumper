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
                    new StringStartsWith(original)
                )
            )
        );
    }
```

In the original code, the `StringContains` constructor requires a single string argument, but it was being called with two arguments `true` and `original`. To fix this, I replaced `new StringContains(true, "Invalid tag")` with `new StringContains("Invalid tag")`, and replaced `new StringContains(false, original)` with `new StringStartsWith(original)`.

Note that `StringStartsWith` is a new method added in the new library version, and it checks if a string starts with a given prefix, which is equivalent to the original `StringContains` call with a negative second argument.