Here's a possible patch for the failing client code:

```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final Matcher<String> matcher = new AllOf<>(
        Arrays.asList(
            new StringContains("Unsupported reference"),
            new StringContains(string)
        )
    );
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(throwable.getMessage(), matcher);
}
```

In this patch, we create a local variable `matcher` to store the `AllOf` matcher, and then pass it directly to `MatcherAssert.assertThat()`. This avoids the need to pass separate arguments to `StringContains`, and should fix the error message.