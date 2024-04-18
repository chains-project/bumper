Here's a possible patch for the failing method:

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
    final StringContains contains = new StringContains(original);
    final Tag.Valid tag = new Tag.Valid(original);
    MatcherAssert.assertThat(tag.valid(), new IsEqual<>(false));
    final InvalidTagNameException exception = Assertions.assertThrows(
        InvalidTagNameException.class,
        tag::value
    );
    MatcherAssert.assertThat(
        exception.getMessage(),
        new AllOf<>(Arrays.asList(
            new StringContains(true, "Invalid tag"),
            contains
        ))
    );
}
```

The change I made is to move the creation of the `StringContains` matcher outside of the call to `MatcherAssert.assertThat()`, so that it can be reused in the `AllOf` matcher. This way, the `true` argument passed to `StringContains` in the `AllOf` matcher can be removed, since it is no longer needed.