Here's a possible patch for the failing method:

```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    ".0",
    "*",
    "\u00ea",
    "-my-tag",
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
                new StringStartsWith("Invalid tag"),
                new StringContains(original)
            )
        )
    );
}
```

The changes made are:

* Replace `StringContains` with `StringStartsWith` for the "Invalid tag" message.
* Replace `new StringContains(true, original)` with `new StringContains(original)` for the `original` string.

The reason for these changes is that the `StringContains` constructor with two arguments has been removed in the new library version, and the constructor with one argument is now used instead. The `StringStartsWith` matcher is used to replace the `StringContains` matcher for the "Invalid tag" message, since it checks if a string starts with a given prefix.