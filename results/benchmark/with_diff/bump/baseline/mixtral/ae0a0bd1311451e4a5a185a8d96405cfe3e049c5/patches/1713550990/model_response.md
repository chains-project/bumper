Here's the updated `shouldFailToGetValueWhenInvalid` method that should fix the error:

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
            ImmutableList.of(
                new StringContains("Invalid tag"),
                new StringContains(original)
            )
        )
    );
}
```

The change is in the `MatcherAssert.assertThat` statement for the message. Instead of using the `StringContains` constructor that takes a `boolean` and a `String`, I used the constructor that takes a `String` and a `Matcher`. The `Matcher` is created using the `StringContains` constructor that takes a `String`. This way, the error message is checked for the substring "Invalid tag" and `original`, without passing the `boolean` value.