Here's the updated method with the required changes:

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
                    new StringContains("Invalid tag"),
                    new StringContains(original)
            )
    );
}
```

In the updated method, I replaced the `StringContains` constructor with the correct one, which only takes a single `String` argument. I also changed the way the `InvalidTagNameException` is assigned to a variable for better readability.