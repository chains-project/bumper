Here's the proposed patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringStartsWith(string + ": Unsupported reference"), new org.hamcrest.core.StringContains(string))));
}
```
The issue is caused by the use of the `StringContains` matcher, which expects a single `String` argument but receives two arguments instead. I replaced `StringContains` with `StringStartsWith` and added the offending `string` value to the expected error message. I also added a new `StringContains` matcher that checks if the error message contains the offending `string` value.