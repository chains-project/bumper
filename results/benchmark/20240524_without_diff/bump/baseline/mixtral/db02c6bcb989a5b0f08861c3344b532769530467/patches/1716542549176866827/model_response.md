Here's the fixed version of the method using the `++` added library method:

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
            new AllOf<>(
                    new StringStartsWith(new IsEqual<>("Invalid tag")),
                    new StringContains(original)
            )
    );
}
```

The change is to replace `StringContains` with `StringStartsWith` to satisfy the new library method signature.