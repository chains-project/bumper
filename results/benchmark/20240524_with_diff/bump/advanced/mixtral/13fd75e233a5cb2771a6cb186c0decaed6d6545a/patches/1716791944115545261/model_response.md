Here's a suggested patch for the given client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), java.lang.Boolean.valueOf(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, () -> tag.value());
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.StringContains(new org.hamcrest.core.AllOf(java.util.Arrays.asList(new org.hamcrest.core.StringStartsWith.StringStartsWith("Invalid tag"), new org.hamcrest.core.StringEndsWith.StringEndsWith(original)))));
}
```

The changes I made are:

1. Replaced `new org.hamcrest.core.IsEqual(false)` with `java.lang.Boolean.valueOf(false)` since `IsEqual` is no longer available.
2. Changed the `tag::value` to `() -> tag.value()` to accommodate the new lambda syntax introduced in the updated library.

These changes should resolve the error you're encountering.