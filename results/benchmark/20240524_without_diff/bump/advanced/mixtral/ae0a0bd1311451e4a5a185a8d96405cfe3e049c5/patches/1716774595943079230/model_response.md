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
        new org.hamcrest.core.StringContains(original) {
            @Override
            protected boolean matchesSafely(final java.lang.String item) {
                return item.contains(original) && !item.equals(original);
            }
        }
    )));
}
```

The patch creates a new anonymous class extending `StringContains` that overrides the `matchesSafely` method to accept the `original` parameter and compare the item to it using `contains` and `!equals` instead of the original constructor's `true` and `false` parameters.