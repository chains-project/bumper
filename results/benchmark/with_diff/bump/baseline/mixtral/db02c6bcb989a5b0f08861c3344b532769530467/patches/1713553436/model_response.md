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
                new StringContains("Invalid tag"),
                new StringStartsWith("Invalid tag"),
                new StringEndsWith(original)
            )
        )
    );
}
```

The changes include:

1. Replacing `new StringContains(true, "Invalid tag")` with `new StringContains("Invalid tag")`.
2. Adding `new StringStartsWith("Invalid tag")` to the `MatcherAssert.assertThat` call.
3. Replacing `new StringContains(false, original)` with `new StringEndsWith(original)`.

These changes address the error message by providing a valid argument list for the `StringContains` constructor and using the new `StringStartsWith` and `StringEndsWith` methods from the updated library version. The test case functionality remains unchanged.