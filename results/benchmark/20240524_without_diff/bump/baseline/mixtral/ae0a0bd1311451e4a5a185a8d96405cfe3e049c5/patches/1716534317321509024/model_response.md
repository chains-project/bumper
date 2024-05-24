Here's the fixed version of the `failsToResolveInvalid` method:

```java
@ParameterizedTest
@ValueSource(strings = {
    "",
    "a:b:c",
    ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContains = new StringContains(string);
    final Throwable throwable = Assertions.assertThrows(
        IllegalStateException.class,
        () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
        throwable.getMessage(),
        AllOf.allOf(
            new StringContains("Unsupported reference"),
            stringContains
        )
    );
}
```

The changes made are:

1. Creating a `StringContains` Hamcrest matcher variable `stringContains` with the `string` input argument.
2. Wrapping the `StringContains` instance in a `AllOf.allOf` matcher.
3. Removing the `true` and `false` arguments from the `StringContains` constructor, using only the `string` argument.

These changes make the code compatible with the new library version, where the `StringContains` constructor no longer accepts a `boolean` argument.