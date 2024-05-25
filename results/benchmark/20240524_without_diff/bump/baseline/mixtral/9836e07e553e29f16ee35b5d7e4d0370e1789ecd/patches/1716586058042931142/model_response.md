Here's the fixed version of the `shouldFailToGetValueWhenInvalid` method:

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

Changes:

1. I replaced `MatcherAssert.assertThat(throwable.getMessage()` with `MatcherAssert.assertThat(e.getMessage()` to get rid of the "cannot be applied to given types" error.
2. I replaced `new StringContains(true, "Invalid tag")` with `new StringStartsWith("Invalid tag")` to resolve the error.

These changes should fix the issue and make the code compile successfully.