Here's a fixed version of the method that should resolve the error:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(
        new org.hamcrest.core.StringContains("Invalid tag"),
        new org.hamcrest.core.StringContains(original)
    )));
}
```

The issue was that the `StringContains` constructor was being called with two arguments, where only one was expected. I've updated the code to pass in a single `AllOf` object that contains two `StringContains` matchers. This should resolve the error.