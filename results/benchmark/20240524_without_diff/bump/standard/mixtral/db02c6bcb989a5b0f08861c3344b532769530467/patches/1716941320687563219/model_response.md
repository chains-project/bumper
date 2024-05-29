Here's the proposed patch for the given failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(
        new org.hamcrest.core.StringContains("Invalid tag"),
        new org.hamcrest.core.StringContains(original)
    )));
}
```

The issue was with the `StringContains` matcher, which expects a single `String` argument, but it was given two arguments `true` and `original`. I replaced it with another `StringContains` matcher that checks if the `throwable` message contains both "Invalid tag" and `original` strings.