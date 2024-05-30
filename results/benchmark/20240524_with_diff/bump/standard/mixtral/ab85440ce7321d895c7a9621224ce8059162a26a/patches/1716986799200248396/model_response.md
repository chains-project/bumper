Here's the proposed patch for the failing client code:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains.ContainingIgnoringCase(string), new org.hamcrest.core.StringContains.StringStartsWith(string))));
}
```

In this patch, I replaced the `StringContains` constructor with `StringContains.ContainingIgnoringCase` and `StringContains.StringStartsWith` constructors to match the new library version. These constructors take a single argument of type `String`, which matches the required argument type for the `StringContains` constructor in the new library version.