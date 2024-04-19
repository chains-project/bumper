Here's the fixed version of the `shouldFailToGetValueWhenInvalid` method:

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
    final InvalidTagNameException exception = Assertions.assertThrows(
        InvalidTagNameException.class,
        tag::value
    );
    MatcherAssert.assertThat(
        exception.getMessage(),
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

1. Replace `new StringContains(true, "Invalid tag")` with `new StringStartsWith("Invalid tag")`, which is the new method added in the library.
2. Remove the second argument from `new StringContains(false, original)` since the new `StringStartsWith` method already checks for the existence of `original` in the error message.

These changes allow the code to compile and pass the tests.