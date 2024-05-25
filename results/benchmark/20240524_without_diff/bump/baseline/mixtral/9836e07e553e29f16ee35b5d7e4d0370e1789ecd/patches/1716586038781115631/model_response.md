Here's a possible patch for the failing method:

```java
    @ParameterizedTest
    @ValueSource(strings = {
        "",
        ".0",
        "*",
        "\u00ea",
        "-my-tag",
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
                    new StringContains(original, false)
                )
            )
        );
    }
```

The changes made are:

* Replace `new StringContains(true, "Invalid tag")` with `new StringContains("Invalid tag")`.
* Replace `new StringContains(false, original)` with `new StringContains(original, false)`.

This should fix the error message by using the correct constructor for `StringContains`.