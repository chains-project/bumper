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
    final InvalidTagNameException e = Assertions.assertThrows(
        InvalidTagNameException.class,
        tag::value
    );
    MatcherAssert.assertThat(
        e.getMessage(),
        new AllOf(
            new ArrayContaining(new StringContains("Invalid tag")),
            not(new StringContains(original))
        )
    );
}
```

The main change is the way the `MatcherAssert.assertThat()` method is called in the last line. Instead of using the `new AllOf<>(Arrays.asList(` constructor, I used the `new AllOf(new ArrayContaining(` constructor. This way, I was able to avoid the error caused by the change in the `StringContains` constructor.

The `ArrayContaining` matcher checks if the provided array contains the given value, and the `not` matcher negates the result. This way, the test checks that the error message contains "Invalid tag", but doesn't contain the original value.

This should fix the error and make the test pass with the updated library version.