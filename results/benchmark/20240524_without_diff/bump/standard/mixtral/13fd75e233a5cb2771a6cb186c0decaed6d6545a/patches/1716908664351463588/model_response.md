Here is the proposed patch:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.HasMessage(new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(
        org.hamcrest.core.StringContains.containsString("Invalid tag"),
        org.hamcrest.core.StringContains.containsStringIgnoringCase(original)
    ))));
}
```

The issue was caused by the incorrect usage of the `StringContains` matcher. I replaced it with the `HasMessage` matcher, which allows to check the exception message more flexibly. I also replaced the `StringContains` matcher with the `StringContains.containsString` and `StringContains.containsStringIgnoringCase` methods, which are more appropriate in this case.