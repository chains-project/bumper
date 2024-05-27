Here is the proposed patch for the failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.StringContains.StringContains(new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringStartsWith.StringStartsWith("Invalid tag"), new org.hamcrest.core.StringEndsWith.StringEndsWith(original))))));
}
```

The error message indicates that the `StringContains` constructor is expecting only one argument, but it is being passed two arguments. To fix this, I replaced the `StringContains` matcher with a `StringContains` instance created using the `StringStartsWith` and `StringEndsWith` matchers. This way, we can still check that the error message contains the substrings "Invalid tag" and "original" without passing two arguments to the `StringContains` constructor.