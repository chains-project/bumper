Here's a suggested patch for the failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.ContainingSubstring("Invalid tag"));
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.StringContains.ContainsString(original));
}
```

The changes made are:

* Replaced the deprecated `StringContains` constructor with the new `StringContains.ContainingSubstring` matcher.
* Added a new `StringContains.ContainsString` matcher to check if the message contains the original string.

Note that the `StringContains.ContainsString` matcher is used instead of `IsEqual` because the error message may contain additional information besides the original string.