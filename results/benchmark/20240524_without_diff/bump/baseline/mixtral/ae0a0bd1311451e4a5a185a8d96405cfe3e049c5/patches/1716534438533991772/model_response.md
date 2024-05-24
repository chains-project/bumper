Here's the patched method:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher matcher = new AllOf<>(
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

The change is in the way the `StringContains` matcher is created. The first argument is now a string instead of a boolean. This is in line with the new library version, which no longer accepts a boolean as the first argument for `StringContains`.