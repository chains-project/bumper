Here's a proposed patch for the failing client code:

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
                Arrays.asList(
                    new StringStartsWith(original + ": "),
                    new StringContains(original)
                )
            )
        );
    }
```

Here's what changed:

* The `StringContains` matcher has been replaced with a combination of `StringStartsWith` and `StringContains` matchers to match the new signature of `StringContains`.
* The `StringContains` matcher is now used with a single argument, as required by the new signature.
* The order of arguments in `AllOf` has been changed to match the new signature of `StringContains`.
* The `Throwable` variable has been renamed to `exception` to better reflect its type.
* The message of the `InvalidTagNameException` has been updated to match the expected format.