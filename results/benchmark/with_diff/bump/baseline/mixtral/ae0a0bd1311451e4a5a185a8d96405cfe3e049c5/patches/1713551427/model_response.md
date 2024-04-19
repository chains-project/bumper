Here's the fixed `failsToResolveInvalid` method:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final HamcrestMatcher stringContains = StringContains.containsString(string);
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains(stringContains),
                            new StringContains(true, "Unsupported reference")
                    )
            )
    );
}
```

The change is to create a `StringContains` matcher variable with the correct constructor argument and use it in the `AllOf` matcher. This way, the issue with the `StringContains` constructor is resolved.