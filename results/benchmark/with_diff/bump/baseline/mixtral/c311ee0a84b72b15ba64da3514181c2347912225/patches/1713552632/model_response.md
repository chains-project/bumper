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
            new AllOf<>(
                    Arrays.asList(
                            new StringContains(true, "Unsupported reference"),
                            stringContains
                    )
            )
    );
}
```

The issue was caused by the fact that the `StringContains` constructor expects a single argument, while the original code was passing two arguments. I've created a separate variable `stringContains` to store the matcher, and then passed it as a single argument to the `AllOf` constructor. This should resolve the compilation error.