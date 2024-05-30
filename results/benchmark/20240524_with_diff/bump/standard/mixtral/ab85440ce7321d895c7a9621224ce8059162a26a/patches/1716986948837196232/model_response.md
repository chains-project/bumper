Here is the proposed patch for the failing client code:
```java
@org.junit.jupiter.params.ParameterizedTest
@org.junit.jupiter.params.provider.ValueSource(strings = { "", "a:b:c", ".123" })
void failsToResolveInvalid(final java.lang.String string) {
    final java.lang.Throwable throwable = org.junit.jupiter.api.Assertions.assertThrows(java.lang.IllegalStateException.class, () -> new com.artipie.docker.ref.ManifestRef.FromString(string).link().string());
    org.hamcrest.MatcherAssert.assertThat(throwable.getMessage(), new org.hamcrest.MatcherAssert.MatchesPattern(new java.util.regex.Pattern("Unsupported reference.*"+string+".*")));
}
```
The failure is caused by the change in the `StringContains` constructor, which now requires only one argument instead of two. To fix this, I replaced the `StringContains` matcher with a `MatchesPattern` matcher that checks if the exception message matches a regular expression pattern. This pattern checks if the message contains the string "Unsupported reference" followed by the input string, which should be sufficient to test the failure case.