Here's a suggested patch for the given client code:

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
        new org.hamcrest.core.StringContains.ContainingIgnoringCase(false, original)
    ))));
}
```

The changes include:

- Replace `throwable.getMessage()` with `throwable` when calling `HasMessage`.
- Replace `StringContains` with `StringContains.Containing` and `StringContains.ContainingIgnoringCase` to match the updated library.
- Add `new` keyword for `StringContains.Containing` and `StringContains.ContainingIgnoringCase` as they are now inner classes.
- Add `.class` to `InvalidTagNameException` in `assertThrows` as it's now a class.
- Add `org.hamcrest.core.AllOf` to `HasMessage` to support multiple matchers.

These changes should resolve the error message you mentioned.