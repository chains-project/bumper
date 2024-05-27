Here's a possible patch for the given client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", ".0", "*", "ê", "-my-tag", // @checkstyle LineLengthCheck (1 line)
"012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678" })
void shouldFailToGetValueWhenInvalid(final java.lang.String original) {
    final com.artipie.docker.Tag.Valid tag = new com.artipie.docker.Tag.Valid(original);
    org.hamcrest.MatcherAssert.assertThat(tag.valid(), new org.hamcrest.core.IsEqual<>(false));
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(com.artipie.docker.error.InvalidTagNameException.class, tag::value);
    org.hamcrest.MatcherAssert.assertThat(throwable, new org.hamcrest.core.HasMessage(
        org.hamcrest.CoreMatchers.allOf(
            org.hamcrest.CoreMatchers.stringContainsString("Invalid tag"),
            org.hamcrest.CoreMatchers.stringContainsString(original)
        )
    ));
}
```

The changes I made are:

* Replace `new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains(true, "Invalid tag"), new org.hamcrest.core.StringContains(false, original)))` with `new org.hamcrest.core.HasMessage(org.hamcrest.CoreMatchers.allOf(org.hamcrest.CoreMatchers.stringContainsString("Invalid tag"), org.hamcrest.CoreMatchers.stringContainsString(original)))`
* Replace `java.util.Arrays.asList` with `org.hamcrest.CoreMatchers.allOf`
* Replace `new org.hamcrest.core.StringContains(true, "Invalid tag")` with `org.hamcrest.CoreMatchers.stringContainsString("Invalid tag")`
* Replace `new org.hamcrest.core.StringContains(false, original)` with `org.hamcrest.CoreMatchers.stringContainsString(original)`