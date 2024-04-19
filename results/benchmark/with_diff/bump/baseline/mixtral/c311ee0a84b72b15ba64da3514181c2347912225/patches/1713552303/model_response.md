Here's the updated `shouldFailToGetValueWhenInvalid` method with the required changes:

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
                new StringContains("Invalid tag"),
                new StringContains(original)
            )
        )
    );
}
```

The changes include:

1. Removed the `true` argument from the first `StringContains` matcher.
2. Changed the `MatcherAssert.assertThat` call for the `throwable.getMessage()` to use the `exception` variable directly.
3. Removed the `Throwable` type from the `assertThrows` method call, using `InvalidTagNameException` instead.