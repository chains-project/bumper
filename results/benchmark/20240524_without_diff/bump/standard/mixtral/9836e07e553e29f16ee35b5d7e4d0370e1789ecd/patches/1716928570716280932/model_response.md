Here's the proposed patch:

```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.core.AllOf<>(java.util.Arrays.asList(new org.hamcrest.core.StringContains(string), new org.hamcrest.core.StringContains.Containing(false, "Unsupported reference"))));
}
```

The failure is caused by an incompatible constructor for `StringContains`. The original code used `new org.hamcrest.core.StringContains(true, "Unsupported reference")`, which takes a boolean and a string. However, the constructor with a boolean argument was deprecated in Hamcrest 2.2 and removed in Hamcrest 2.5.

To fix the issue, I replaced the `StringContains` constructor with `new org.hamcrest.core.StringContains(string)` and used `new org.hamcrest.core.StringContains.Containing(false, "Unsupported reference")` to replace the deprecated constructor. This ensures that the code is compatible with newer versions of Hamcrest.