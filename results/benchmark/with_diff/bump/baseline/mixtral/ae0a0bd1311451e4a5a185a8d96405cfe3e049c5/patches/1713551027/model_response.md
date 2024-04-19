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

The change is in the `StringContains` constructor. Instead of using `new StringContains(true, "Invalid tag")`, we now use `new StringContains("Invalid tag")`. The first argument, `containsString`, is now inferred as `true` because it is the first argument in the constructor. This resolves the error message regarding the constructor's argument list length.