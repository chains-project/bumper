Here's a possible patch for the failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(
        new org.hamcrest.core.StringContains.Containing(true, "Invalid tag"),
        new org.hamcrest.core.StringContains.ContainsString(false, original)
    )));
}
```

The change I made is to replace the `new org.hamcrest.core.StringContains(true, "Invalid tag")` and `new org.hamcrest.core.StringContains(false, original)` with `new org.hamcrest.core.StringContains.Containing(true, "Invalid tag")` and `new org.hamcrest.core.StringContains.ContainsString(false, original)` respectively.

The reason for this change is that the `StringContains` constructor now requires a single argument of type `String` instead of two arguments of type `boolean` and `String`. The `Containing` and `ContainsString` matchers are used to achieve the same functionality.