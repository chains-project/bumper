Here's a potential patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains("Unsupported reference"), new org.hamcrest.core.StringStartsWithIgnoringCase(string))));
}
```
In this patch, I replaced the `StringContains` matcher with `StringStartsWithIgnoringCase` matcher to avoid the compilation error. This matcher checks if the input string starts with the given substring, ignoring case. This should achieve similar functionality to the original code while avoiding the dependency update issue.