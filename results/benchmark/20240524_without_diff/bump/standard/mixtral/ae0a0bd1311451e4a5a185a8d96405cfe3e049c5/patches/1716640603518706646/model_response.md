Here's a fixed version of the given method with a minor modification:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, () -> tag.value());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.CoreMatchers().<java.lang.String>allOf(new org.hamcrest.core.StringContains.CoreStringContains(original), new org.hamcrest.core.StringContains.CoreStringContains("Invalid tag")));
}
```
The issue was with the `assertThrows` method call. I replaced the `tag::value` expression with a lambda expression `() -> tag.value()`. This is because the `assertThrows` method expects a `Executable` object that can be invoked without any arguments.