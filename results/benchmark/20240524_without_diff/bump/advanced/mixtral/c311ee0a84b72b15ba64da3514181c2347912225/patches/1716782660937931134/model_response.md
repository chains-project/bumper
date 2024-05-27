Here's the fixed method with the error resolved:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.CoreMatchers.AllOf(Arrays.asList(
            org.hamcrest.core.StringContains.containsString("Invalid tag"),
            org.hamcrest.core.StringContains.containsString(original) == false
    )));
}
```

The issue was caused by using `new org.hamcrest.core.StringContains(true, "Invalid tag")` and `new org.hamcrest.core.StringContains(false, original)`. Instead, I replaced them with `org.hamcrest.core.StringContains.containsString("Invalid tag")` and `org.hamcrest.core.StringContains.containsString(original) == false` respectively.