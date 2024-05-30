Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains.StringContains(string), new org.hamcrest.core.StringContains.ContainsString(string))));
}
```
The failure is caused by the change in the `StringContains` constructor, which now requires only a single argument (a `String`) instead of the previous two arguments (a `boolean` and a `String`). To fix the failure, I have replaced the usage of `StringContains` with two new instances of `StringContains`, one using the `StringContains` constructor that takes a `String` argument, and the other using the `ContainsString` constructor that takes a `String` argument. This change allows the code to be compatible with the new version of the library.