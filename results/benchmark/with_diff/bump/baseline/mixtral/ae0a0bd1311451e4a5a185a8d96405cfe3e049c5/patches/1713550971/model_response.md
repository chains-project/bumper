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

The changes include:

1. Replacing the `StringContains` matcher with `StringStartsWith` to satisfy the constructor requirements.
2. Removing the `true` argument from the `StringContains` matcher, as it is not necessary in the updated library version.
3. Renaming the `throwable` variable to `exception` for better readability.
4. Updating the `StringContains` matcher to accept a single argument.

These changes should resolve the error message and allow the test to compile and run successfully with the new library version.