Here is the proposed patch for the failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.StringContains("Invalid tag"));
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.StringContains.StringContains(original));
}
```

The changes made to the original code are:

* Replace `new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains(true, "Invalid tag"), new org.hamcrest.core.StringContains(false, original)))` with `new org.hamcrest.core.StringContains.StringContains("Invalid tag")` and `new org.hamcrest.core.StringContains.StringContains(original)`.

The reason for this change is that the constructor for `StringContains` has changed in the new library version. The original code was using the constructor `StringContains(boolean containsPrefix, String substring)`, which has been removed in the new version. The new constructor `StringContains(String substring)` has been added, which takes a single `String` argument. This is why we can replace the original code with the new code.

Note that the fully qualified names for the `StringContains` class have been used (`org.hamcrest.core.StringContains.StringContains`) to avoid any potential ambiguity.