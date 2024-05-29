Here is a possible patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.ContainingSubstring("Invalid tag"));
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.StringContains.ContainsSubstring(original));
}
```
I replaced the `org.hamcrest.core.StringContains` matcher with `org.hamcrest.core.StringContains.ContainingSubstring` and `org.hamcrest.core.StringContains.ContainsSubstring` to avoid the error caused by the change in the constructor signature of `org.hamcrest.core.StringContains`.

These two matchers have a similar behavior to `org.hamcrest.core.StringContains`, but they only check if the given string contains the expected substring, instead of checking if it is equal to it.

This should fix the error and allow the test to pass.