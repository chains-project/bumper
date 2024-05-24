Here's a possible patch for the failing method:

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
        new AllOf<>(
            Arrays.asList(
                new StringContains(true, "Unsupported reference"),
                stringContains
            )
        )
    );
}
```

The change is to create a local variable `stringContains` for the `StringContains` matcher, and pass it directly to the `AllOf` matcher, instead of using the constructor with a boolean argument. This way, the `StringContains` constructor is called with the correct number of arguments.