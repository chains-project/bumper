Here's a potential patch for the given client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.HasMessage(new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(
            new org.hamcrest.core.StringContains.Containing("Invalid tag"),
            new org.hamcrest.core.StringContains.ContainsString(original)))));
}
```

The patch replaces the `IsEqual` matcher with `HasMessage` and creates a new `StringContains` object with the `Containing` factory method, passing a string argument instead of a boolean. This resolves the error message by providing the correct number of arguments to the `StringContains` constructor.