Here's the fixed version of the code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.StringContains(new org.hamcrest.core.StringStartsWith("Invalid tag")));
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.StringDoesNotContain.StringDoesNotContain(original));
}
```

The issue was caused by using an incorrect constructor for `StringContains` in the `assertThat` method. I replaced it with the `StringContains` matcher and added two additional `StringDoesNotContain` and `StringStartsWith` matchers to ensure the error message contains the "Invalid tag" prefix and doesn't contain the original input.