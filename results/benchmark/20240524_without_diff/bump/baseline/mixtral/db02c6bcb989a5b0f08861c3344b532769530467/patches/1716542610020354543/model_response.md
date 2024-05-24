Here's a patch that you can apply to fix the error:

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

* Replaced the deprecated `StringContains(boolean, String)` constructor with the `StringContains(String)` constructor.
* Assigned the `Throwable` returned by `Assertions.assertThrows()` to a variable of type `InvalidTagNameException` for type consistency in the following assertion.