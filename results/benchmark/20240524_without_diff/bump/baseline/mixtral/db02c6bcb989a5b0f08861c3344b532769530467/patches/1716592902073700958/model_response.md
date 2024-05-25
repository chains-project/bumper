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
            allOf(
                stringContains("Invalid tag"),
                stringContainsIgnoringCase(original)
            )
        );
    }
```

The changes made:

* Replaced `new StringContains(true, "Invalid tag")` with `stringContains("Invalid tag")`
* Replaced `new StringContains(false, original)` with `stringContainsIgnoringCase(original)`

Note: `stringContains` and `stringContainsIgnoringCase` are Hamcrest matchers that are added in newer versions of Hamcrest. They are equivalent to `new StringContains(true, "Invalid tag")` and `new StringContains(false, original)` respectively.