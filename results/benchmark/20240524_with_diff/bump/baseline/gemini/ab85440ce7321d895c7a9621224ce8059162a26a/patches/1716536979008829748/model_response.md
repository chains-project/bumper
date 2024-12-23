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
        final Throwable throwable = Assertions.assertThrows(
            InvalidTagNameException.class,
            tag::value
        );
        final String message = throwable.getMessage();
        assertThat(message.contains("Invalid tag"), is(true));
        assertThat(message.contains(original), is(false));
    }
```