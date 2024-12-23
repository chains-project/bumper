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
    MatcherAssert.assertThat(tag.valid(), is(false));
    final Throwable throwable = Assertions.assertThrows(
            InvalidTagNameException.class,
            tag::value
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            allOf(
                    Arrays.asList(
                            containsString("Invalid tag"),
                            not(containsString(original))
                    )
            )
    );
}
```