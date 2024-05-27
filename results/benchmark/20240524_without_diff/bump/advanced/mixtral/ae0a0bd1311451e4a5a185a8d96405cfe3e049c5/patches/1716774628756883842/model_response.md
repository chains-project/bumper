Here's a possible patch for the failing client code:

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
            org.hamcrest.CoreMatchers.not(org.hamcrest.CoreMatchers.stringContainsIgnoringCase(original)))
    ));
}
```

In this patch, I replaced the `StringContains` matcher with a `HasMessage` matcher, which allows for more flexibility in matching the exception message. I used the `allOf` method from `CoreMatchers` to combine two separate `stringContains` and `stringContainsIgnoringCase` matchers, which should achieve the same effect as the original code.

Note that the `HasMessage` matcher matches the entire exception message, so the order of the two sub-matchers matters. In this case, I put the `stringContains` matcher before the `stringContainsIgnoringCase` matcher to ensure that the "Invalid tag" substring is present in the message, regardless of the case of the original string.