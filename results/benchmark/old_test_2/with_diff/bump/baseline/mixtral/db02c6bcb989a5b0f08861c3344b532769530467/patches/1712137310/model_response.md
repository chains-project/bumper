Here's a possible patch for the failing client code:

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
            new AllOf(
                new ArrayContaining(
                    new StringDescription("Invalid tag"),
                    new StringDescription(original)
                )
            )
        );
    }
```

In this patch, I replaced the `StringContains` matcher with the `ArrayContaining` matcher, which accepts an array of `StringDescription` objects that describe the expected substrings in the exception message. This way, we can avoid the error caused by the `StringContains` constructor that now requires only one argument.