Here's the proposed patch:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual(false));
    java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    StringContains stringContains = new org.hamcrest.core.StringContains("Invalid tag", false);
    stringContains.describeMismatch(throwable.getMessage(), new org.hamcrest.StringDescription());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf(stringContains,
            new org.hamcrest.core.StringContains(false, original)));
}
```

The issue in the original code is that the `<org.hamcrest.MatcherAssert.CoreMatchers().<java.lang.String>allOf(` line is not syntactically correct. It seems like the intention was to create a matcher using `allOf`, but the syntax used is incorrect.

In the proposed patch, I created a separate `StringContains` variable for the "Invalid tag" matcher and used it in the `allOf` matcher along with the second `StringContains` matcher. This should achieve the same functionality as the original code, but with correct syntax.