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
            () -> {
                try {
                    tag.value();
                } catch (final InvalidTagNameException e) {
                    MatcherAssert.assertThat(
                        e.getMessage(),
                        new AllOf<>(
                            Arrays.asList(
                                new StringContains(true, "Invalid tag"),
                                new StringContains(false, original)
                            )
                        )
                    );
                    throw e;
                }
            }
        );
    }
```