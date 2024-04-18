Here's the updated `shouldFailToGetValueWhenInvalid` method with the necessary changes to fix the error:

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

The main change is in the way the `StringContains` matcher is used. Instead of passing `true` and `false` as the first and second arguments, respectively, the expected substring ("Invalid tag") is passed as the only argument. This way, the error related to the method signature of `StringContains` is resolved.