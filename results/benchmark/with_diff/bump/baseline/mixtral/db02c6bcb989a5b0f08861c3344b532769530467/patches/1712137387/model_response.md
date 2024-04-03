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
    final Matcher<String> matcher = new StringContains(original);
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
                new StringContains(new IsEqual<>("Invalid tag")),
                matcher
            )
        )
    );
}
```

The changes made are:

* Create a `matcher` variable to store the `StringContains` matcher, so that it can be reused later.
* Use the `IsEqual` matcher for the "Invalid tag" string instead of passing `true` to `StringContains`.
* Use the `matcher` variable instead of passing `false` to `StringContains`.

This should fix the error message by using the correct arguments for the `StringContains` constructor.