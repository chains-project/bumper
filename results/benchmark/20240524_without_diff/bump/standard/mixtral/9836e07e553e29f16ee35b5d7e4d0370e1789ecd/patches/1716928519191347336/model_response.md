Here's the fixed failing method:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains("Unsupported reference"), new org.hamcrest.core.StringStartsWithIgnoringCase(string))));
}
```

In this patch, I replaced the `StringContains` matcher with a `StringStartsWithIgnoringCase` matcher from the same `org.hamcrest.core` package. This resolves the error message by using a matcher that accepts the correct number of arguments.