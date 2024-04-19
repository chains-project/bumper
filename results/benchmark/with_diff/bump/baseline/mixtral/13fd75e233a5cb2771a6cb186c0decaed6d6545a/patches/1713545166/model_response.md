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
        new AllOf(
            new ArgumentMatcher<>("Invalid tag", message -> message.contains("Invalid tag")),
            new ArgumentMatcher<>("original", message -> !message.contains(original))
        )
    );
}

private static class ArgumentMatcher<T, U> implements ArgumentMatcher<String> {
    private final T value;
    private final U condition;
    private final BiPredicate<T, U> matcher;

    public ArgumentMatcher(T value, BiPredicate<T, U> matcher) {
        this.value = value;
        this.matcher = matcher;
        this.condition = null;
    }

    public ArgumentMatcher(String description, BiPredicate<T, U> matcher) {
        this.value = null;
        this.matcher = matcher;
        this.condition = description;
    }

    @Override
    public boolean matches(String s) {
        return matcher.test(value, condition != null ? condition : value);
    }

    @Override
    public String toString() {
        if (condition == null) {
            return String.valueOf(value);
        }
        return String.format("%s %s", condition, value);
    }
}
```

The main change here is that I've created a custom `ArgumentMatcher` class to replace the `StringContains` matcher that was causing the error. This new class allows you to pass in a description and a predicate function to define the custom matcher. This way, you can use the `AllOf` matcher as before, but with your custom matchers instead of the removed `StringContains` matcher.