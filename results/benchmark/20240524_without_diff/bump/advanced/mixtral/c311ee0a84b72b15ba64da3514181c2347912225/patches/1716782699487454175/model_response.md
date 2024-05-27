Here's the proposed patch for the failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.ContainsSubstring("Invalid tag"));
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.StringContains.ContainsString(original));
}
```

The issue with the original code is that the `StringContains` constructor expects a single `String` argument, but it was being called with two arguments - a `boolean` and a `String`. I've replaced the two `StringContains` matchers with a single `ContainsSubstring` matcher for the "Invalid tag" message, and a `ContainsString` matcher for the original string.