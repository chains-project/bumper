Here is a possible patch for the code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.CoreMatchers.<java.lang.String>allOf(new org.hamcrest.core.StringContains.CoreStringContains(original), new org.hamcrest.core.StringContains.CoreStringContains("Invalid tag")));
}
```
The error message indicates that the `StringContains` constructor is expecting a single `String` argument, but it is receiving two arguments: a `boolean` and a `String`. This is because the `allOf` method of `MatcherAssert` is expecting a variable number of `Matcher` arguments, but it is receiving a variable number of `Object` arguments.

To fix this, we need to use the `CoreMatchers` class to create a `CoreStringContains` matcher for the `original` string, and another `CoreStringContains` matcher for the "Invalid tag" string. Then, we can use the `allOf` method of `MatcherAssert` to combine these matchers into a single matcher.

This should resolve the error and allow the code to compile and run successfully.