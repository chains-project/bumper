Here's a possible patch for the failing method:

```java
@ParameterizedTest
@ValueSource(strings = {
        "",
        "a:b:c",
        ".123"
})
void failsToResolveInvalid(final String string) {
    final Throwable throwable = Assertions.assertThrows(
            IllegalStateException.class,
            () -> new ManifestRef.FromString(string).link().string()
    );
    MatcherAssert.assertThat(
            throwable.getMessage(),
            new AllOf<>(
                    Arrays.asList(
                            new StringContains("Unsupported reference"),
                            new StringStartsWith(string)
                    )
            )
    );
}
```

In this patch, I replaced the `StringContains` matcher with `StringStartsWith` matcher, which takes only one argument and matches if the given string starts with the argument. This matcher was added in the new library version and can be used instead of `StringContains`.