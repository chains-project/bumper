Here's the fixed version of the `shouldFailToGetValueWhenInvalid` method:

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
        new AllOf(
            new ArrayContains(new StringDescription("Invalid tag"), new String[]{exception.getMessage()})
        )
    );
}
```

In the original code, the `StringContains` matcher was used incorrectly, providing a boolean flag to indicate whether the matcher should ignore case sensitivity. Instead, you should use the `ArrayContains` matcher with a `StringDescription` for the expected value and the actual exception message. This way, the `StringContains` constructor's argument list length issue is resolved.