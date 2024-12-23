```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    final boolean containsInvalidTag = throwable.getMessage().contains("Invalid tag");
    final boolean containsOriginal = throwable.getMessage().contains(original);
    org.hamcrest.MatcherAssert.assertThat(containsInvalidTag, new org.hamcrest.core.IsEqual<>(true));
    org.hamcrest.MatcherAssert.assertThat(containsOriginal, new org.hamcrest.core.IsEqual<>(false));
}
```