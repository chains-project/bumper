Here's the updated `shouldFailToGetValueWhenInvalid` method that should fix the error:

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
        new AllOf(
            ImmutableList.of(
                new StringContains(e.getMessage(), "Invalid tag"),
                new StringContains(e.getMessage(), original)
            )
        )
    );
}
```

The main change is the way we pass the arguments to `StringContains`. In the new version of the library, the constructor of `StringContains` accepts only one argument, the expected substring. Previously, it accepted two arguments: the first one was a boolean indicating whether the substring should be present (`true`) or absent (`false`), and the second one was the expected substring itself.

To fix the error, I created a new `InvalidTagNameException` instance `e` from the result of the `assertThrows` method. Then, I updated the `MatcherAssert.assertThat` call for the `throwable.getMessage()` to use the new constructor of `StringContains` with the correct argument: the expected substring `original`. Additionally, I wrapped the `StringContains` matcher in an `AllOf` matcher to ensure both conditions are checked.