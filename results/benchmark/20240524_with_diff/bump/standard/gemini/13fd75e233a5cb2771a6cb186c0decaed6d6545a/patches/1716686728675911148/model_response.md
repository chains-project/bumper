```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    final boolean containsUnsupportedReference = throwable.getMessage().contains("Unsupported reference");
    final boolean doesNotContainString = !throwable.getMessage().contains(string);
    org.junit.jupiter.api.Assertions.assertTrue(containsUnsupportedReference && doesNotContainString, "Message should contain 'Unsupported reference' but not the string itself");
}
```