Here's the updated code that should fix the error:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.HasMessage(org.hamcrest.CoreMatchers.allOf(
        org.hamcrest.CoreMatchers.stringContains("Invalid tag"),
        org.hamcrest.CoreMatchers.stringContainsIgnoringCase(original)
    )));
}
```

I replaced the `StringContains` matcher with `HasMessage` that accepts a `Matcher<String>` as a parameter. I then created two separate `stringContains` and `stringContainsIgnoringCase` matchers, which should solve the issue.